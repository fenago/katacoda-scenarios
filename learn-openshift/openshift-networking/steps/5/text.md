

Now that the first project is ready, let's create another one:
`oc new-project demo-4`{{execute}}

Like we did previously, create a pod from the same YAML definition as before:
`oc create -f httpd-pod.yml`{{execute}}

And create a service by exposing the pod:
`oc expose po/httpd --port 80`{{execute}}


Now, let's open a bash session into the newly created pod and try to reach the pod from the demo-1 project:


`oc exec httpd -it bash`{{execute}}

`dig httpd.demo-3.svc.cluster.local`{{execute}}

```
httpd.demo-1.svc.cluster.local. 30 IN A 172.30.35.41
```

For the sake of completeness, let's switch the project to demo-1 and try the same from the first pod:


`oc project demo-3`{{execute}}

```
Now using project "demo-1" on server "https://openshift-master.example.com:8443".
```

`oc exec httpd -it bash`{{execute}}

`dig httpd.demo-4.svc.cluster.local`{{execute}}


It's even possible to get all endpoints of a particular service, although it's recommended to use services as points of contact:
`dig httpd.demo-4.endpoints.cluster.local`{{execute}}


**Note:**
OpenShift injects cluster-level subdomains into the local resolver's configuration at /etc/resolv.conf, so if you take a look in that file, you will find the line search <project>.svc.cluster.local svc.cluster.local cluster.local. Therefore, FQDNs don't have to be specified in order to reach resources across a project's boundaries and in the same project. For example, you can use httpd.demo-1 to call a service named httpd in the demo-1 project, or just httpd if it's in the same project.

As you can see, both pods can reach each other via their services, which makes it possible not to rely on environment variables. So, in order to migrate their applications to OpenShift, developers will have to configure environment variables of their applications to point to the DNS names of dependent services. 
