
Now, let's see what happens if we try to create one more pod. Prepare a new pod definition from the one used to create the first pod by replacing nginx with httpd:


`cat httpd-pod.yml
apiVersion: v1
kind: Pod
metadata:
  name: httpd
  labels:
    role: web
spec:
  containers:
  - name: httpd
    image: httpd
    resources:
      requests:
        cpu: 400m
        memory: 128Mi
If we try to create the second pod, we will see the following:


`create -f httpd-pod.yml`{{execute}}

Error from server (Forbidden): error when creating "httpd-pod.yml": pods "httpd" is forbidden: exceeded quota: my-quota, requested: pods=1, used: pods=1, limited: pods=1
Even though the amount of requested memory wouldn't violate the quota, pod creation was still denied because the quota limits the total number of pods to 1 for the current project.

Edit the quota to allow 2 pods and 2 CPU cores:


`oc edit quota/my-quota
spec:
  hard:
    cpu: 500m
    memory: 256Mi
    pods: "2"
    resourcequotas: "1"
Try creating the second pod again:


`oc create -f httpd-pod.yml
pod "httpd" created
It worked because the quota was set to allow 2 pods in the current project.

Let's see how many resources are used from the total allowed by the quota again:


`oc describe quota/my-quota`{{execute}}
Name:            my-quota
Namespace:       myproject
Resource         Used    Hard
--------         ----    ----
cpu              500m    500m
memory           256Mi   256Mi
pods             2       2
resourcequotas   1       1

As you can see, we have exhausted the entire quota and no new pods can be created.

Now that this exercise is over, it's time to prepare for the next one by cleaning up our lab:


`oc delete all --all`{{execute}}


`oc delete quota/my-quota`{{execute}}
