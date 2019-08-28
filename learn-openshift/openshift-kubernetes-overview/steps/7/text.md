
As with Docker, we can run a Kubernetes pod with the kubectl run command. Let's start with a simple web server example:
`kubectl run httpd --image=httpd`{{execute}}

We can verify the result by getting a list of Kubernetes pods, by running the kubectl get pods command:
`kubectl get pods`{{execute}}

```
NAME                      READY    STATUS    RESTARTS    AGE
httpd-8576c89d7-qjd62      1/1     Running    0          6m
```


Note
The first time you run this command, you will probably see that the Kubernetes pod status shows up as ContainerCreating. What is happening behind the scenes is that the Docker httpd image is being downloaded to Minikube VM. Be patient and give it some time to download the image. A few minutes later you should be able to see the container status is Running.  The kubectl run command does more than just download an image and run a container out of it. We are going to cover this later in this chapter. The 8576c89d7-qjd62 part is generated automatically. We are going to discuss this later in this chapter.

Essentially, this pod is a Docker container inside our Minikube VM, and we can easily verify this. First, we need to ssh into Minikube VM with minikube ssh, and then run the docker ps command:
`minikube ssh`{{execute}}

`docker ps`{{execute}}

We can try to kill this httpd Docker container, but Kubernetes will automatically spawn the new one:
`docker rm -f container-id`{{copy}}

Check the container status one more time:
`docker ps`{{execute}}

Note that the httpd container is still up, but with another ID. The initial ID was c52c95f4d241 and it became 5e5460e360b6 (you will have other IDs). That is one of the benefits of Kubernetes: if one container dies, Kubernetes will bring in a new one automatically. We are going to discuss this in detail later in this chapter.