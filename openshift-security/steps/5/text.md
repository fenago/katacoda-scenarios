To complete this step, define a pod called `mypod` and with that pod define a container called `myfrontend`, which is based on the official `nginx:latest` docker image. We will send request to nginx at this port.

Also, define _volumeMounts_ with name `pvol` and use _mountPath_ as `/logs`. We will also use claim `claim1` created in the previous step.

OpenShift finds the claim with the given name and then uses the claim to find the volume to mount.

Create nginx pod by running `oc create -f pod.yaml`{{execute HOST1}}

You can see the name of the pods corresponding to the running containers for this application, by running:
``oc get pods``{{execute HOST1}}

You only have one instance of the application so only one pod will be listed.


Security context constraints

Another mechanism for controlling the behavior of pods is security context constraints (SCCs). These cluster-level resources define what resources can be accessed by pods and provide an additional level of control. By default, OpenShift supports seven SCCs:
`oc login -u system:admin`{{execute}}

`oc get scc`{{execute}}

```
anyuid                ...
hostaccess            ...
hostmount-anyuid      ...
hostnetwork           ...
nonroot               ...
privileged            ...
restricted            ...
```

You may notice anyuid SCC we used in the subsection "Creating custom roles" to solve the problem with container's permissions.

By default, all pods, except those for builds and deployments, use a default service account assigned by the restricted SCC, which doesn't allow privileged containers – that is, those running under the root user and listening on privileged ports (<1024).

Use docker inspect to see what user is specified in the nginx image metadata:


`docker inspect nginx`{{execute}}

```
[
    {
...
<output omitted>
...
            "User": "",
...
<output omitted>
...
    }
]
```
Coincidentally, the metadata doesn't specify the user, which makes the image run as root. This is exactly what restricted SCC is designed to prevent.

Previously, we just assigned the anyuid SCC to a default service account, which means that ALL containers get to run as privileged, and that is a big security risk. A good practice is to create a dedicated service account for our pod/container, so let's do this the right way:
`oc create sa myserviceaccount

Next, we have to assign the anyuid SCC to this account, but to do so we must login as the cluster administrator first:


`oc adm policy add-scc-to-user anyuid -z myserviceaccount`{{execute}}

```
scc "anyuid" added to: ["system:serviceaccount:myproject:myserviceaccount"]
```