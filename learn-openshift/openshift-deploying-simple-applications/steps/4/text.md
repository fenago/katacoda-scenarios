The following YAML file allows you to define a Service OpenShift object:

           
<pre class="file" data-filename="svc-httpd.yml" data-target="replace">
apiVersion: v1
kind: Service
metadata:
  labels:
    name: httpd
  name: httpd
spec:
  ports:
  - port: 8080
    protocol: TCP
    targetPort: 8080
  selector:
    name: httpd
</pre>

Once the file is in place, you can create the service by running the following command:


`oc create -f svc-httpd.yml`{{execute}}


`oc get svc`{{execute}}

The service shows the same output as previously described:
`curl -s http://172.30.112.133:8080 | head -n 4`{{execute}}


Creating a route
The service allows an application to be accessible internally via a consistent address:port pair. To be able to access it from outside of the cluster, we need to make sure that an OpenShift Route is created. Once the route is created, OpenShift will expose the service to the outside world using the cluster's router, implemented via an HAProxy Docker container by default.

Like services, routes can be created in two ways:

Using oc expose
From the YAML/JSON definition
This section shows both methods, but it is enough to use only one.

We assume that previously, you created a service named httpd. 

Creating a route by using oc expose
You can create a route using oc expose in the following way:


`oc expose svc httpd`{{execute}}


`oc get route`{{execute}}



`curl -s http://httpd-simpleappication.127.0.0.1.nip.io | head -n 4`{{execute}}


`oc delete route httpd`{{execute}}


Creating a route from a YAML definition
Let's create an alternate route for our application named httpd2. The route will have the myhttpd.example.com URL:

<pre class="file" data-filename="route-httpd2.yml" data-target="replace">
apiVersion: v1
kind: Route
metadata:
 labels:
 name: httpd2
 name: httpd2
spec:
 host: myhttpd.example.com
 port:
 targetPort: 8080
 to:
 kind: Service
 name: httpd
 weight: 100
</pre>

The route may be created by oc create:
`oc create -f route-httpd2.yml`{{execute}}

`oc get route`{{execute}}

You may see that the new route has been added successfully. Now, if there is a corresponding DNS record, you will be able to access your application using that alternate route.