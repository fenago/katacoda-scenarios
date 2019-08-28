
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


Let's create a pod using a Docker image with the kubectl run command:
`kubectl run httpd --image=docker.io/httpd`{{execute}}

**Note:**
We need to specify a full path to a Docker image since CRI-O is a universal Runtime Interface and it does not know whether we want to use Docker or any other container technology registry. 


Wait for a minute or so while Kubernetes downloads the httpd image and then verify that we have a httpd pod up and running:
`kubectl get pods`{{execute}}


Again, from this point of view, it looks pretty standard, but if we run the kubectl describe command, we will see that the container ID starts with cri-o://:
`kubectl describe pods/httpd-7dcb9bd6c4-x5dhm`{{execute}}

At this point, this shows us that Kubernetes is using the CRI-O runtime interface. This means that Kubernetes is talking to CRI-O. CRI-O (the crio daemon, to be specific) is handling the image pulling and container creating processes. Let's verify this by running the docker images and docker ps commands inside the Minikube VM:


`minikube ssh docker images`{{execute}}

`minikube ssh docker ps`{{execute}}

```
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
```


As you can see, there are no images or containers named httpd. 