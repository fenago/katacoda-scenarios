OpenShift services represent an interface between clients and the actual application running in the pods. A service is an IP:port pair which forwards traffic to backend pods in a round-robin fashion.

By running the oc new-app command, OpenShift creates a service automatically. We can verify this by running the oc get services command:
`oc get services`{{execute}}

We can delete and recreate this service again by running the oc delete and oc expose commands. Before we do that, run the curl command inside the Minishift VM to verify that the service is up and running:


`curl -I -m3 http://[[HOST_IP]]::8080`{{execute}}

...
<output omitted>
...
0 0 0 0 0 0 0 0 --:--:-- --:--:-- 0 HTTP/1.1 200 OK
...
<output omitted>
...

The status code is 200, which means that the web page is available and the service is running properly:
`oc delete svc/ruby-ex`{{execute}}


Check that the service is deleted and that the service is no longer available:
`oc get svc`{{execute}}


`minishift ssh "curl -I -m3 172.30.173.195:8080"
...
<output omitted>
...
Command failed: exit status 28


Now, create a new service with the oc expose command by coping and running:
`oc expose pods/<pod-name>`{{copy}}

**Note:** In your case, the container name is going to be different. Rerun `oc get pods`{{execute}} to get the running pod name.

`oc get svc`{{execute}}


Finally, check that the service is available again by running the curl command on the Minishift VM:
`curl -I -m3 http://[[HOST_IP]]::8080`{{execute}}
