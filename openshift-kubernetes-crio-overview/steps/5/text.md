
It's time to get hands-on with CRI-O. We are not going to explore CRI-O in depth, but rather show you how to bring up a development environment with CRI-O configured with some basic functionality. 


Let's bring down your virtual environment:

`minikube stop`{{execute}}

```
Stopping local Kubernetes cluster...
Machine stopped.
And delete the Minikube VM:
```

`minikube delete`{{execute}}

```
Deleting local Kubernetes cluster...
Machine deleted.
```

**Note:** At the time of writing, CRI-O is still under development. Therefore, the setup instructions in your case might be a bit different and you will need to refer to the official Minikube documentation.  
