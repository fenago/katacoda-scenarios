Clearing the virtual environment
Once you are done working with Kubernetes, you can easily stop the Minikube cluster by running the minikube stop command:
`minikube stop`{{execute}}

```
Stopping local Kubernetes cluster...
Machine stopped.
```

After that, you can delete the Minikube VM if you want by running the minikube delete command:
`minikube delete`{{execute}}

Verify that the Minikube cluster no longer exists:
`minikube status`{{execute}}

minikube:
cluster:
kubectl:
