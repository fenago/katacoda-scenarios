Separating configuration from application code using ConfigMaps
The ConfigMap resource is used to separate data from a pod running an application. These kinds of resource contain arbitrary data to be injected into a pod as configuration. Injection in this context means that the pod can use it in the following ways:

#### Export its key/value pairs as environment variables
Supply its values as command-line arguments to the application
Mount it as a volume inside the pod to the location where the application expects to find its configuration file

Let's look at the process of exporting ConfigMap as an environment variable into a container. First, we have to create ConfigMap itself from a list of environment variables:


<pre class="file" data-filename="example.env" data-target="replace">
VAR_1=Hello
VAR_2=World
</pre>

`oc create cm example-config-map --from-env-file=example.env`{{execute}}


Use the following command to see what the actual resource looks like:
`oc describe configmap/example-config-map`{{execute}}


Now we are ready to inject it into a pod. Create a simple Pod definition that references the newly created ConfigMap:

<pre class="file" data-filename="example-pod-1.yml" data-target="replace">
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
</pre>

And create the pod using the preceding definition:
`oc create -f example-pod-1.yml`{{execute}}

Since the command is a simple Linux command, env, not a process or listening server of any kind, the pod exits right after it's completed, but you can still see its logs:
`oc logs po/example`{{execute}}

```
...
<output omitted>
...
VAR_1=Hello
VAR_2=World
```

As you can see, the two environment variables we defined in ConfigMap were successfully injected into the container. If we were to run an application inside our container, it could read them.

The same method can be used to supply these variables as command-line arguments to the container command. First, let's delete the old pod:
`oc delete po/example`{{execute}}

Then, create a new pod definition so that you can use the variables as command-line arguments to echo the command:

<pre class="file" data-filename="example-pod-2.yml" data-target="replace">
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
</pre>


Now, create a container from the updated definition:
`oc create -f example-pod-2.yml`{{execute}}

As we mentioned previously, the container will exit right after the command returns, but its logs will contain the output of the command, constructed of two variables from our ConfigMap:

`oc logs po/example2`{{execute}}

```
Hello World
```

Lastly, we will walk-through mounting ConfigMap as a configuration file into a pod. Again, let's delete the pod from the previous exercise:
`oc delete po/example2`{{execute}}
