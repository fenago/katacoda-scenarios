Installing and working with CRI-O
It's time to get hands-on with CRI-O. We are not going to explore CRI-O in depth, but rather show you how to bring up a development environment with CRI-O configured with some basic functionality. 

Stopping your virtual environment
Before you move on to the next chapter, bring down your virtual environment:


`minikube stop`{{execute}}
Stopping local Kubernetes cluster...
Machine stopped.
And delete the Minikube VM:


`minikube delete
Deleting local Kubernetes cluster...
Machine deleted.

**Note:**
At the time of writing, CRI-O is still under development. Therefore, the setup instructions in your case might be a bit different and you will need to refer to the official Minikube documentation.  

In order to start Kubernetes with CRI-O as a Container Runtime Interface, we are going to use Minikube with an additional --container-runtime crio option:


`minikube start --container-runtime crio`{{execute}}
Starting local Kubernetes v1.9.0 cluster...
...
<output omitted>
...
Loading cached images from config file.
Check Minikube's status and make sure that it is up and running:


`minikube status`{{execute}}
minikube: Running
cluster:  Running
kubectl:  Correctly Configured: pointing to minikube-vm at 192.168.99.106
It looks pretty standard, but if we take a look at the Minikube logs, we will see that Minikube is initializing CRI-O Runtime:


`minikube logs | grep cri-o`{{execute}}
Jul 08 21:11:36 minikube localkube[3098]: I0708 21:11:36.333484 3098 kuberuntime_manager.go:186] Container runtime cri-o initialized, version: 1.8.4, apiVersion: v1alpha1
Let's create a pod using a Docker image with the kubectl run command:


`kubectl run httpd --image=docker.io/httpd`{{execute}}
deployment "httpd" created
**Note:**
We need to specify a full path to a Docker image since CRI-O is a universal Runtime Interface and it does not know whether we want to use Docker or any other container technology registry. 

Wait for a minute or so while Kubernetes downloads the httpd image and then verify that we have a httpd pod up and running:
`kubectl get pods`{{execute}}


Again, from this point of view, it looks pretty standard, but if we run the kubectl describe command, we will see that the container ID starts with cri-o://:
`kubectl describe pods/httpd-7dcb9bd6c4-x5dhm`{{execute}}

Name: httpd-7dcb9bd6c4-x5dhm
...
<output omitted>
...
IP: 10.1.0.4
Container ID: crio://3f2c2826318f1526bdb9710050a29b5d4a3de78d61e0...
Image: docker.io/httpd
...
<output omitted>
...
At this point, this shows us that Kubernetes is using the CRI-O runtime interface. This means that Kubernetes is talking to CRI-O. CRI-O (the crio daemon, to be specific) is handling the image pulling and container creating processes. Let's verify this by running the docker images and docker ps commands inside the Minikube VM:


`minikube ssh docker images`{{execute}}

`minikube ssh docker ps`{{execute}}

CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES

As you can see, there are no images or containers named httpd. We mentioned earlier that CRI-O is using runc Container Runtime behind the scenes. To help us further with the verification process, we are going to use the runc command inside the Minikube VM. runc is a CLI command for running containers packaged according to the OCI format. The syntax of the runc command is very similar to the docker command we used in Chapter 1, Containers and Docker Overview.


`minikube ssh "sudo runc ps 3f2c2826318f1526bdb9710050a29b5d4a3de78d61e07ac9d83cedb9827c62e4"`{{execute}}

UID PID PPID C STIME TTY TIME CMD
root 5746 5695 0 02:39 ? 00:00:00 httpd -DFOREGROUND
daemon 5788 5746 0 02:39 ? 00:00:00 httpd -DFOREGROUND
daemon 5792 5746 0 02:39 ? 00:00:00 httpd -DFOREGROUND
daemon 5793 5746 0 02:39 ? 00:00:00 httpd -DFOREGROUND


**Note:** that 3f2c2826318f1526bdb9710050a29b5d4a3de78d61e07ac9d83cedb9827c62e4 is the container ID from the kubectl describe pods/httpd-7dcb9bd6c4-x5dhm command we ran previously.