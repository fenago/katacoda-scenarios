
Describing Kubernetes resources 
We can quickly take a look at the internals of this pod by running the kubectl describe command:


`kubectl describe pod httpd-8576c89d7-qjd62`{{execute}}

Name: httpd
Namespace: default
Node: minikube/192.168.99.101
Start Time: Sat, 10 Mar 2018 00:01:33 -0700
Annotations: <none>
Status: Running
IP: 172.17.0.4
...
<output omitted>
...
It gives us enough information to efficiently locate the pod and do the proper troubleshooting when necessary. In our case, we can ssh to Minikube VM and run the curl command to check if the pod is running the web server properly. 

Note
You may need to use another IP address for the curl command; in our case it is 172.17.0.4, derived from the kubectl describe command output.


`minikube ssh`{{execute}}


`curl 172.17.0.4`{{execute}}

```
<html><body><h1>It works!</h1></body></html>
```


`exit`{{execute}}


Note that this pod is accessible only inside the Kubernetes cluster. That is the reason why we need to log in to Minikube VM. If we try to access this address from our local PC, it will not work. We are going to discuss this in the following sections.
 
The command to get a list of exposed Kubernetes services is kubectl get services:
`kubectl get services`{{execute}}


Note that port 80 was mapped to dynamic port 31395 on the Minikube VM. The port is dynamically chosen in the range 30000–32767.Also, there is a ClusterIP field with the IP address 10.110.40.149 allocated for the httpd-expose service. Do not pay attention to this at the moment; we are going to discuss this later in the book.

Finally, use curl to check if the httpd server is available from the outside of the Kubernetes cluster:


`curl 192.168.99.101:31395`{{execute}}
<html><body><h1>It works!</h1></body></html>
If you open this link in your web browser, you should see It works! on the web page.