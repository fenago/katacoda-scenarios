Working with kubectl
Kubectl is a command-line interface for managing a Kubernetes cluster and its resources. In this section, you will learn about the most common commands and their use cases.

The syntax for all the commands follows this convention:


`kubectl <COMMAND> <RESOURCE_TYPE> <RESOURCE_NAME> <OPTIONS>
Commands in angle brackets <> mean the following:

COMMAND: An action to be executed against one or more resources.
RESOURCE_TYPE: The type of resource to be acted upon, for example, a pod or service.
RESOURCE_NAME: The name of the resource(s) to manage.
OPTIONS: Various flags used to modify the behavior of kubectl commands. They have higher priority than default values and environment variables, thus overriding them.
Getting help
kubectl has hundreds of different subcommands, options, and arguments. Luckily, kubectl has really good help options. The first one is man pages. If you are using macOS or Linux, you can run the man-f kubectl command to check kubectl-related man pages:


`man -f kubectl
kubectl(1) - kubectl controls the Kubernetes cluster manager
kubectl-alpha(1), kubectl alpha(1) - Commands for features in alpha
kubectl-alpha-diff(1), kubectl alpha diff(1) - Diff different versions of configurations
...
<output omitted>
...
If for some reason you do not have man pages available on your system, you can just run the kubectl command without any options or arguments. It will show you a list of available subcommands:


`kubectl
kubectl controls the Kubernetes cluster manager.
Find more information at https://github.com/kubernetes/kubernetes.
Basic Commands (Beginner):
  create Create a resource from a file or from stdin.
  expose Take a replication controller, service, deployment or pod and expose it as a new Kubernetes Service
...
<output omitted>
...
Basic Commands (Intermediate):
 get Display one or many resources
 explain Documentation of resources
...
<output omitted>
...
Use "kubectl <command> --help" for more information about a given command.
Use "kubectl options" for a list of global command-line options (applies to all commands)
The next step is to check the list of available resources by running kubectl <command> or kubectl <command> --help commands, for example, kubectl get:


`kubectl get
  * all
  * certificatesigningrequests (aka 'csr')
  * clusterrolebindings
...
<output omitted>
...
Use "kubectl explain <resource>" for a detailed description of that resource (e.g. kubectl explain pods).
See 'kubectl get -h' for help and examples.
As you can see, you can also get kubectl get command examples by running kubectl get -h and a detailed resource explanation by running kubectl explain pods. The kubectl command is very easy to navigate and work with.

Using the kubectl get command
The first essential command to run is kubectl get nodes. It gives us the number of Kubernetes nodes available:


`kubectl get nodes
NAME      STATUS  ROLES   AGE   VERSION
minikube   Ready   <none> 2h    v1.9.0
In our case, the number of nodes will be equal to one, since we are using one VM for our practice. As we mentioned already, in order for different projects to coexist on the same or different nodes, namespaces are used. You may guess that the command we should use is kubectl get namespaces:


`kubectl get namespaces
NAME          STATUS   AGE
default       Active   15h
kube-public   Active   15h
kube-system   Active   15h
It shows you that three default namespaces are available when you install Kubernetes with Minikube:

Name                                 

Description

default

The namespace where all resources without other namespaces are placed. It is used when the name of a namespace is not specified.

kube-public

Used for resources that must be publicly available even to unauthenticated users.

kube-system

As the name implies, it is used internally by Kubernetes itself for all system resources.

The last main missing component here is pods; as previously mentioned, pods represent a collection of containers and a pod is a basic management unit in Kubernetes. In our case, pods are Docker containers. We do not have any running pods yet, which can be easily verified by kubectl get pods:


`kubectl get pods`{{execute}}

No resources found.
It says No resources found, all because the pod is a Kubernetes resource, similar to other resources we are going to cover in this book.

Note
Similarly to kubectl get pods, you can get the status of any other Kubernetes resource. We will discuss other Kubernetes resources later in this chapter.  

Running Kubernetes pods
As with Docker, we can run a Kubernetes pod with the kubectl run command. Let's start with a simple web server example:


`kubectl run httpd --image=httpd`{{execute}}

We can verify the result by getting a list of Kubernetes pods, by running the kubectl get pods command:
`kubectl get pods`{{execute}}


Note: The first time you run this command, you will probably see that the Kubernetes pod status shows up as ContainerCreating. What is happening behind the scenes is that the Docker httpd image is being downloaded to Minikube VM. Be patient and give it some time to download the image. A few minutes later you should be able to see the container status is Running.  The kubectl run command does more than just download an image and run a container out of it. We are going to cover this later in this chapter. The 8576c89d7-qjd62 part is generated automatically. We are going to discuss this later in this chapter.

Essentially, this pod is a Docker container inside our Minikube VM, and we can easily verify this. First, we need to ssh into Minikube VM with minikube ssh, and then run the docker ps command:


`minikube ssh`{{execute}}
$
`docker ps`{{execute}}


CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
c52c95f4d241 httpd "httpd -g 'daemon ..." 12 minutes ago Up 12 minutes k8s_httpd-container_httpd_default_39531635-23f8-11e8-ab32-080027dcd199_0
...
<output omitted>
...
We can try to kill this httpd Docker container, but Kubernetes will automatically spawn the new one:
`docker rm -f c52c95f4d241`{{execute}}

Check the container status one more time:
`docker ps`{{execute}}



Note: The httpd container is still up, but with another ID. The initial ID was c52c95f4d241 and it became 5e5460e360b6 (you will have other IDs). That is one of the benefits of Kubernetes: if one container dies, Kubernetes will bring in a new one automatically. We are going to discuss this in detail later in this chapter.

Describing Kubernetes resources 
We can quickly take a look at the internals of this pod by running the kubectl describe command:
`kubectl describe pod httpd-8576c89d7-qjd62`{{execute}}

It gives us enough information to efficiently locate the pod and do the proper troubleshooting when necessary. In our case, we can ssh to Minikube VM and run the curl command to check if the pod is running the web server properly. 

Note: You may need to use another IP address for the curl command; in our case it is 172.17.0.4, derived from the kubectl describe command output.

`minikube ssh`{{execute}}


`curl 172.17.0.4`{{execute}}

<html><body><h1>It works!</h1></body></html>

`exit`{{execute}}


Note: Note that this pod is accessible only inside the Kubernetes cluster. That is the reason why we need to log in to Minikube VM. If we try to access this address from our local PC, it will not work. We are going to discuss this in the following sections.

Editing Kubernetes resources
We can also edit the properties of a running container with kubectl edit pod httpd-8576c89d7-qjd62. We are not going to change anything at this point, but you can try to change something before we delete the container. We are going to work with the edit command while working with OpenShift in further chapters.

Note
The kubectl edit command by default uses the vi editor. Learn how to use vi first if you are not familiar with this text editor, otherwise you might get into trouble.  Another trick that you can do is to change the editor by running export EDITOR=nano, where nano is your favorite text editor.

Similarly, you can edit any other Kubernetes resources. We will discuss other Kubernetes resources later in this chapter.  

Exposing Kubernetes services
When we run a pod using the kubectl run command, this pod is accessible only inside Kubernetes. In most of cases, we would want this pod to be accessible from the outside as well. This is where the kubectl expose command comes in handy. Let's create the httpd pod one more time and then expose it to the outside world:


`kubectl run httpd --image=httpd`{{execute}}

`kubectl get pods`{{execute}}

Now let's use the kubectl expose command and expose the httpd web server to the outside of Kubernetes:


`kubectl expose pod httpd-66c6df655-8h5f4 --port=80 --name=httpd-exposed --type=NodePort`{{execute}}

While using the kubectl expose command, we specify several options:
- **port**: Pod (Docker container) port that we are going to expose to the outside of the Kubernetes cluster.
- **name**: Kubernetes service name.
- **type**: Kubernetes service type. NodePort uses Kubernetes Node IP.  

The command to get a list of exposed Kubernetes services is kubectl get services:
`kubectl get services`{{execute}}

Note: Port 80 was mapped to dynamic port 31395 on the Minikube VM. The port is dynamically chosen in the range 30000–32767.Also, there is a ClusterIP field with the IP address 10.110.40.149 allocated for the httpd-expose service. Do not pay attention to this at the moment; we are going to discuss this later in the book.

Finally, use curl to check if the httpd server is available from the outside of the Kubernetes cluster:
`curl 192.168.99.101:31395`{{execute}}

<html><body><h1>It works!</h1></body></html>

If you open this link in your web browser, you should see It works! on the web page.

Using Kubernetes labels
When you have an application that consists of one pod and one service, there is no problem operating these resources. But when your application grows, or you have tens or hundreds of projects, pods, services and other Kubernetes resources, it will get harder to operate and effectively troubleshoot Kubernetes. This is where we can use the Kubernetes labels we mentioned earlier in this chapter. We are going to run a couple more Kubernetes pods using labels:


`kubectl run httpd1 --image=httpd --labels="app=httpd-demo1"`{{execute}}

`kubectl run httpd2 --image=httpd --labels="app=httpd-demo2"`{{execute}}

Check the Kubernetes pods we have at the moment:
`kubectl get pods`{{execute}}

Now, imagine you have at least 10 or more pods. In order to efficiently filter out this output, we can use the -l option:
`kubectl get pods -l="app=httpd-demo2"`{{execute}}

```
NAME                   READY       STATUS      RESTARTS       AGE
httpd2-5b4ff5cf57-9llkn 1/1         Running    0              2m
```

**Note:** Filtering out output with Kubernetes labels is not the only use case. Labels are also used alongside selectors. You can get more information on both topics using the Kubernetes official documentation at https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/.

Deleting Kubernetes resources
If we've done something wrong with the pod, or it may have broken for some reason, there is a simple way to delete a pod using the kubectl delete pod command:
`kubectl delete pod httpd-8576c89d7-qjd62`{{execute}}

pod "httpd-8576c89d7-qjd62" deleted
We can delete all pods using the --all option:
`kubectl delete pod --all`{{execute}}

**Note:** if you run kubectl get pods, you will see all the containers running again. The reason for this is that, when we run the kubectl run command, it creates several different Kubernetes resources, which we are going to discuss in the following section.

We can delete Kubernetes resources by running kubectl delete all with the -l option:
`kubectl delete all -l app=httpd-demo1`{{execute}}


deployment "httpd1" deleted
pod "httpd1-c9f7d7fd9-d9w94" deleted

`kubectl get pods`{{execute}} 


This command will delete all Kubernetes with a httpd-demo1 label only. The other two pods will be still available.

Alternatively, we can delete all Kubernetes resources we have created so far by running the kubectl delete all --all command:


`kubectl delete all --all`{{execute}}

deployment "httpd" deleted
deployment "httpd2" deleted
pod "httpd-8576c89d7-ktnwh" deleted
pod "httpd2-5b4ff5cf57-t58nd" deleted
service "kubernetes" deleted
service "nginx-exposed" deleted
Kubernetes advanced resources
When we create an application with the kubectl run command, it takes care of several things. Let's create an httpd pod by running this command one more time and take a deeper look at what actually happens behind the scenes:


`kubectl run httpd1 --image=httpd`{{execute}}
We can take a look at the series of events that took place during this process by running the kubectl get events command. It shows you what Kubernetes did behind the scenes to launch this application. You will see quite a long list, which may seem confusing at first glance, but we can narrow it down by using the following command: 


`kubectl get events --sort-by=.metadata.creationTimestamp | tail -n 8`{{execute}}
4s 4s ... kubelet, minikube pulling image "httpd"
4s 4s ... replicaset-controller Created pod: httpd1-6d8bb9cdf9-thlkg
4s 4s ... default-scheduler Successfully assigned httpd1-6d8bb9cdf9-thlkg to minikube
4s 4s ... deployment-controller Scaled up replica set httpd1-6d8bb9cdf9 to 1
4s 4s ... kubelet, minikube MountVolume.SetUp succeeded for volume "default-token-dpzmw"
2s 2s ... kubelet, minikube Created container
2s 2s ... kubelet, minikube Successfully pulled image "httpd"
2s 2s ... kubelet, minikube Started containe