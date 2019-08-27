Autoscaling your application depending on CPU and RAM utilization
You can scale pods in your application using the oc scale command, but it has two disadvantages:

It has to be run manually every time you need to scale a pod up or down
You have to take into account CPU and RAM utilization yourself
This approach doesn't allow businesses to adapt quickly to constantly changing customers demands. There is a better way—HorizontalPodAutoscaler.

Note
At the time of writing, autoscaling can only track CPU and RAM usage. Traffic-based autoscaling, for instance, isn't supported.

Let's login as system:admin and see if Hawkular, Cassandra, and Heapster pods are up and running:


`oc login -u system:admin`{{execute}}
...
<output omitted>
...
`oc get po -n openshift-infra`{{execute}}

NAME                       READY STATUS  RESTARTS AGE
hawkular-cassandra-1-ffszl 1/1   Running 0        10m
hawkular-metrics-bl6jh     1/1   Running 0        10m
heapster-brvfd             1/1   Running 0        10m
Note
By the time you get to this section, all metrics pods will be ready, but usually it takes 8-10 minutes for them to get started after installation is done.

CPU-based autoscaling
CPU-based autoscaling also requires limit ranges to be set on CPU requests for the pods being scaled, so we can use the LimitRange definition from one of the previous sections.


`cat my-limits.yaml 
apiVersion: v1
kind: LimitRange
metadata:
  name: my-limits
spec:
  limits:
    - type: Pod
      min:
        cpu: 50m
        memory: 64Mi
      max:
        cpu: 150m
        memory: 128Mi
    - type: Container
      min:
        cpu: 50m
        memory: 64Mi
      max:
        cpu: 150m
        memory: 128Mi

`oc create -f my-limits.yaml
limitrange "my-limits" created
Note
Depending on your host machine's CPU, you might have to tweak the values in the file above in order for autoscaling to work, that is why in the listing above they are different than in the beginning of the chapter.

The autoscaling feature can be applied to deployment configs, so the easiest way to create one is to use the already familiar new-app command:


`oc new-app httpd
...
<output omitted>
...
--> Creating resources ...
    deploymentconfig "httpd" created
    service "httpd" created
--> Success
    Application is not exposed. You can expose services to the outside world by executing one or more of the commands below:
     'oc expose svc/httpd' 
    Run 'oc status' to view your app.
For demonstration purposes, we used the Apache web server image to create an image stream, which, in turn, is used to create the application. Now that the deploymentconfig is ready to manage pods, we can create a HorizontalPodAutoscaler to manage the deploymentconfig itself:


`oc autoscale dc/httpd --min=2 --max=4 --cpu-percent=10`{{execute}}
deploymentconfig "httpd" autoscaled

Note: We specified 2 as the minimum number of pods that must be maintained at any time so that you can observe the effect of autoscaling quickly without having to generate CPU load on pods to trigger it. We will do that in a few moments as well.

Let's make sure it was created:


`oc get hpa`{{execute}}

NAME   REFERENCE              TARGETS   MINPODS MAXPODS REPLICAS  AGE
httpd  DeploymentConfig/httpd 0% / 20%  2       4       2         3m
Note
If you run this command right after creation, you will most likely see unknown instead of 0% in the preceding output. That is expected because HorizontalPodAutoscaler usually needs a few minutes to collect enough metrics.

In a few minutes, you may list running pods and notice that there are two of them now:
`oc get po`{{execute}}

NAME            READY     STATUS    RESTARTS   AGE
httpd-1-5845b   1/1       Running   0          7s
httpd-1-scq85   1/1       Running   0          2m

Now, we have to simulate a large number of user requests to our pods to increase the CPU load so that autoscaling takes effect. But to do that, we need to create a route first:
`oc expose svc/httpd`{{execute}}

`oc get route`{{execute}}
... httpd-advanced.openshift.example.com ...
At this point, we have everything we need, so let's start simulating CPU load with the ab Apache benchmarking utility:

`apt-get update && apt-get install apache2-utils`{{execute}}

`ab -c 100 -n 10000000 -H 'Host: httpd-advanced.openshift.example.com' http://127.0.0.1/`{{execute}}

```
...
<output omitted>
...
^C
Percentage of the requests served within a certain time (ms)
  50% 46
  66% 56
  75% 66
  80% 73
  90% 95
  95% 124
  98% 171
  99% 200
 100% 528 (longest request)
```


When httpd DeploymentConfig is scaled up, you can just press Ctrl+C to stop generating the traffic, as is indicated by ^C in the output above.

Login in a separate terminal as system:admin and at some point you should be able to see that you have 4 pods running :
`oc get po`{{execute}}

Once you press Ctrl + C and benchmarking stops, then after a while, the number of pods will go back to normal:
`oc get po`{{execute}}

NAME            READY     STATUS    RESTARTS   AGE
httpd-1-5wsb5   1/1       Running   0          35m
httpd-1-gvqg2   1/1       Running   0          34m
If you are interested, you can see the collected metrics and autoscaling taking place in the web console. Open the webconsolein a browser at https://openshift.example.com:8443/, confirm the security exception for the self-signed certificate, and login with the usernamealiceand any password.

As our OpenShift cluster uses self-signed TLS certificates for encrypting HTTP traffic, Hawkular metrics will not be accessible from the Overview tab of the web console at first—you will see an error above the list of pods instead. To fix this, click on the provided link to open the Hawkular URL in a separate tab/window in your browser and confirm the security exception for the certificate as well. After that, refresh the Overview tab and you will see the calculated metrics for each pod marked with different colors:


You can also use the Monitoring tab to get a more detailed view:


You can clearly see the spikes in CPU load and network traffic that correspond to the ab run. We need to delete CPU-based autoscaler before the next exercise:


`oc delete hpa/httpd`{{execute}}

horizontalpodautoscaler "httpd" deleted
Memory-based autoscaling
Unlike autoscaling based on CPU utilization, memory-based autoscaling can only be enabled by creating a HorizontalPodAutoscaler from a raw YAML/JSON definition:


`cat hpa-memory.yml`{{execute}}

kind: HorizontalPodAutoscaler
apiVersion: autoscaling/v1
metadata:
  name: hpa-httpd-memory
spec:
  scaleTargetRef:
    apiVersion: v1
    kind: DeploymentConfig
    name: httpd
  minReplicas: 2
  maxReplicas: 4
  metrics:
  - type: Resource
    resource:
      name: memory
      targetAverageUtilization: 10
Let's enable autoscaling now:


`oc create -f hpa-memory.yml`{{execute}}

horizontalpodautoscaler "hpa-httpd-memory" created
Give it a minute or two to pick up the metrics from Heapster and you will be able to see how the current memory utilization is different from the target:


`oc get hpa`{{execute}}

NAME      REFERENCE  TARGETS   MINPODS MAXPODS          ... 
hpa-httpd-memory DeploymentConfig/httpd 7% / 10%  2  4  ...
Note
If you run this command right after creation, you will most likely see unknown instead of 7% in the preceding output. This is expected because HorizontalPodAutoscaler usually needs a few minutes to collect sufficient metrics.

Let's go ahead and generate traffic for the application, just like in the previous section, but establish 1000 concurrent connections this time, instead of 100:


`ab -c 1000 -n 10000000 -H 'Host: httpd-advanced.openshift.example.com' http://127.0.0.1/`{{execute}}



Note: Leave benchmark open for 5-10 minutes, and meanwhile open your browser at https://hawkular-metrics.openshift.example.com/hawkular/metrics to make sure that hawkular metrics are running, and then at https://openshift.example.com:8443/console/project/advanced/overview

You can observe autoscaling taking place from the web console. First it scales our web server to 3 replicas:


And shortly after, to 4:


After ab is finished generating traffic, the number of pods slowly goes down:


Note
It is possible to observe short bursts in the number of replicas if you put too much load on the service. This is normal and you may see from events that the deploymentconfig scales, for example, from 3 to 6 without transient states, then quickly detects the anomaly and corrects it by scaling back to the maximum value.Due to the specifics of memory utilization by pods, it's common that the deploymentconfig/replicationcontroller doesn't fully scale back to the minimum number of replicas.

The exercise is over, so it's time to clean-up:

`oc delete all --all`{{execute}}

`oc delete limits/my-limits`{{execute}}
limitrange "my-limits" deleted