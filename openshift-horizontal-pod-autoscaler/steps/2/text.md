Autoscaling your application depending on CPU and RAM utilization


You can scale pods in your application using the oc scale command, but it has two disadvantages:
- It has to be run manually every time you need to scale a pod up or down
- You have to take into account CPU and RAM utilization yourself.


This approach doesn't allow businesses to adapt quickly to constantly changing customers demands. There is a better way—HorizontalPodAutoscaler.

Note: Autoscaling can only track CPU and RAM usage.Traffic-based autoscaling, for instance, isn't supported.

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


Note: By the time you get to this section, all metrics pods will be ready, but usually it takes 8-10 minutes for them to get started after installation is done.