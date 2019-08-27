OpenShift pods are Kubernetes pods that represent a collection of containers, and each pod serves as a basic management unit. All containers in a pod share the same storage volumes and network. In order to get a list of pods in OpenShift, we can use the oc get pods command:
`oc get pods`{{execute}}

It is no different from the Kubernetes pod, which means behind the scenes it is a Docker container running. The only difference is that there are two containers now. One of them is a container (ruby-ex-1-build) that is used to build the final image with the source code applied. We can easily verify this by running the docker ps command:

`docker ps`{{execute}}

We can easily find the right running container by seeing the myproject/ruby-ex part of the image's ID. We can do similar actions in Kubernetes, like getting logs, editing or describing, and deleting pods.

Separating configuration from application code using ConfigMaps
The ConfigMap resource is used to separate data from a pod running an application. These kinds of resource contain arbitrary data to be injected into a pod as configuration. Injection in this context means that the pod can use it in the following ways:

Export its key/value pairs as environment variables
Supply its values as command-line arguments to the application
Mount it as a volume inside the pod to the location where the application expects to find its configuration file
Before you begin, make sure you are logged in as an unprivileged user for the most representative experience:


`oc login -u alice`{{execute}}
Let's look at the process of exporting ConfigMap as an environment variable into a container. First, we have to create ConfigMap itself from a list of environment variables:


`cat example.env`{{execute}}
VAR_1=Hello
VAR_2=World

`oc create cm example-config-map --from-env-file=example.env
configmap "example-config-map" created
Use the following command to see what the actual resource looks like:


`oc describe configmap/example-config-map`{{execute}}
Name: example-config-map
Namespace: advanced
Labels: <none>
Annotations: <none>

Data
====
VAR_1:
----
Hello
VAR_2:
----
World
Events: <none>
Now we are ready to inject it into a pod. Create a simple Pod definition that references the newly created ConfigMap:


`cat example-pod-1.yml`{{execute}}
apiVersion: v1
kind: Pod
metadata:
  name: example
spec:
  containers:
    - name: example
      image: cirros
      command: ["/bin/sh", "-c", "env"]
      envFrom:
        - configMapRef:
            name: example-config-map
And create the pod using the preceding definition:


`oc create -f example-pod-1.yml`{{execute}}
pod "example" created
Note
As you learned in Chapter 2, Kubernetes Overview, OpenShift supports YAML and JSON notations for resource definitions; in this book, we rely primarily on the former. As a reminder of the YAML syntax, you can refer to the link at http://www.yaml.org/start.html. No matter if you use YAML or JSON, the OpenShift REST API supports very specific fields that vary between resource types and are documented in https://docs.openshift.org/latest/rest_api/api/.

Since the command is a simple Linux command, env, not a process or listening server of any kind, the pod exits right after it's completed, but you can still see its logs:


`oc logs po/example`{{execute}}
...
<output omitted>
...
VAR_1=Hello
VAR_2=World
As you can see, the two environment variables we defined in ConfigMap were successfully injected into the container. If we were to run an application inside our container, it could read them.

The same method can be used to supply these variables as command-line arguments to the container command. First, let's delete the old pod:


`oc delete po/example`{{execute}}
pod "example" deleted
Then, create a new pod definition so that you can use the variables as command-line arguments to echo the command:


`cat example-pod-2.yml`{{execute}}
apiVersion: v1
kind: Pod
metadata:
  name: example2
spec:
  containers:
    - name: example2
      image: cirros
      command: ["/bin/sh", "-c", "echo ${VAR_1} ${VAR_2}"]
      envFrom:
        - configMapRef:
            name: example-config-map
Now, create a container from the updated definition:


`oc create -f example-pod-2.yml`{{execute}}

As we mentioned previously, the container will exit right after the command returns, but its logs will contain the output of the command, constructed of two variables from our ConfigMap:

`oc logs po/example2`{{execute}}
Hello World

Lastly, we will walk-through mounting ConfigMap as a configuration file into a pod. Again, let's delete the pod from the previous exercise:


`oc delete po/example2`{{execute}}
pod "example2" deleted

