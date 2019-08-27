Now it's time to create a pod that will use this ConfigMap. Create yet another pod definition with the following structure:


`cat example-pod-3.yml`{{execute}}
apiVersion: v1
kind: Pod
metadata:
  name: example3
  labels:
    role: web
spec:
  containers:
  - name: example3
    image: nginx
    volumeMounts:
    - name: conf
      mountPath: /etc/nginx/conf.d
  volumes:
  - name: conf
    configMap:
      name: nginx
      items:
      - key: nginx_custom_default.conf
        path: default.conf
Note
You can specify a path parameter in configMap.items to provide the name for the file that the configuration will be stored in. Had we not done that in the preceding example, the file name would have been the same as the key from the configMap–nginx_custom_default.conf. We must specify the label for our pod in order to be able to create a service for it later on.

Let's create the pod now:


`oc create -f example-pod-3.yml`{{execute}}
pod "example3" created
In order to see whether the server listens on the port specified in the ConfigMap, we could open a bash session inside the pod and see if the configuration file is in place, but let's use a better way that will let us practice with OpenShift resources more.

We will need to create a service for this pod and then expose it. First, create a service:


`oc expose po/example3 --port 8888`{{execute}}
service "example3" exposed
Note
We had to explicitly specify the port in the command because we didn't provide it in the containerPort parameter in the pod's definition.

Then expose the service itself through route:


`oc expose svc/example3`{{execute}}
route "example3" exposed
`oc get route
... example3-advanced.openshift.example.com ...
Finally, we can use the curl command to request a default web page from the server's default virtual host:


`curl -H 'Host: example3-advanced.openshift.example.com' 127.0.0.1`{{execute}}
...
<output omitted>
...
<title>Welcome to nginx!</title>
...
<output omitted>
...
Note
We could have created a separate record for the route above in /etc/hosts, pointing to 127.0.0.1, but in order to keep the environment as clean as possible, it's a good practice to use Host HTTP header instead to select a particular application.

The preceding output indicates that Nginx indeed listens on port 8888/tcp, as specified in the ConfigMap. This concludes our exercise with ConfigMaps, so let's clean up our lab:


`oc delete all --all`{{execute}}
route "example3" deleted
pod "example3" deleted
service "example3" deleted

`oc delete configmap --all`{{execute}}
configmap "example-config-map" deleted
configmap "nginx" deleted
Note
ConfigMaps are not considered similar to other resources such as pods or services and must be deleted separately.