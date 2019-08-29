In this step, we will learn OpenShift CLI using the command _oc_.

Before we begin, make sure that your OpenShift is up and running. Let's login as system:admin user since managing quotas & limits requires admin privileges:
`oc login -u system:admin`{{execute}}

# Output

```
Login successful.

You don't have any projects. You can try to create a new project, by running

    oc new-project <projectname>
```

To create a new project called ``advanced`` run the command:

`oc new-project advanced`{{execute}}

One of the main ideas behind OpenShift projects in multi-tenant environments is the need to limit resource consumption at a more granular level than just a whole cluster, providing operations with the ability to scope such limitations to organizations and departments.

OpenShift provides two mechanisms for setting limits on resource consumption in a cluster:
- ResourceQuota
- LimitRanges


Manual application deployment
Among other methods, OpenShift allows for deploying applications directly from existing Docker images. Imagine that your development team has an in-house process of building Docker images from their applications—this way, you can deploy applications in an OpenShift environment by using these images without any modification, which greatly simplifies migration to OpenShift. It takes several steps to create all required OpenShift entities.

First, you have to create a pod, which runs a container deployed from the application's Docker image. Once the pod is up and running, you may need to create a service to have a persistent IP address and internal DNS record associated with it. The service allows your application to be accessible via a consistent address:port pair internally inside OpenShift. This may be enough for internal applications that don't require external accesses, like databases or key/value storage.

If your application has to be available from the outside, you need toexposeit to make it available from an external network, like the internet. This process can be achieved by creating an OpenShift route.

In short, the process looks like this:

- Create a pod
- Create a service by exposing the pod
- Create a route by exposing the service

In this scenario, we will be working with a simple httpd Docker container to demonstrate the application deployment process. We have chosen httpd because it is simple enough and it still allows us to focus on the main goal—the demonstration of OpenShift-related tasks.

Creating a pod

The httpd Docker image is available on Docker Hub. You may want to confirm this by running the following command:
`docker search httpd`{{execute}}

```
INDEX NAME DESCRIPTION STARS OFFICIAL AUTOMATED
docker.io docker.io/httpd The Apache HTTP Server Project 1719 [OK]
<OMITTED>
According to the image documentation (https://docs.docker.com/samples/library/httpd/), it listens on TCP port 80. We cannot simply use this container, because it binds to a privileged port. The default security policy in OpenShift doesn't allow applications to bind on ports below 1024. To avoid problems, OpenShift comes with an image stream named httpd which points to an OpenShift-ready httpd image build. For example, in our version of OpenShift, the httpd image stream points to the docker.io/centos/httpd-24-centos7 Docker container. You may want to verify that by running the following command:
```

`oc get is -n openshift | egrep "^NAME | ^httpd"`{{execute}}

```
NAME DOCKER REPO TAGS UPDATED
httpd 172.30.1.1:5000/openshift/httpd latest,2.4 3 hours ago
```

`oc describe is httpd -n openshift | grep "tagged from"`{{execute}}
  tagged from centos/httpd-24-centos7:latest
Each time we want to deploy a pod using an httpd image, we need to use centos/httpd-24-centos7 instead. 

Let's create a separate project for the lab as follows:


`oc new-project simpleappication`{{execute}}
Now using project "simpleappication" on server "https://localhost:8443".
<OMITTED>
The simple httpd pod can be deployed manually from its definition:

<pre class="file" data-filename="pod_httpd.yml" data-target="replace">
apiVersion: v1
kind: Pod
metadata:
  name: httpd
  labels:
    name: httpd
spec:
  containers:
    - name: httpd
      image: centos/httpd-24-centos7
      ports:
        - name: web
          containerPort: 8080
</pre>

Note
centos/httpd-24-centos7 binds on port 8080, which allows for running the container inside OpenShift without tuning its default security policy.

Once the file is created, we can create a pod by running oc create:


`oc create -f pod_httpd.yml`{{execute}}

OpenShift needs some time to download the Docker image and deploy the pod. Once everything is finished, you should be able to have the httpd pod in the Running state:
`oc get pod`{{execute}}

```
NAME READY STATUS RESTARTS AGE
httpd 1/1 Running 0 2m
```

This pod provides the same functionality as a more complex application would (default httpd web page). We may want to verify that, as shown as follows.

First, get the pod's internal IP address:


`oc describe pod httpd | grep IP:`{{execute}}


And then use curl to query the IP from the output above:
`curl -s http://172.17.0.2:8080 | head -n 4`{{execute}}

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
 <head>



**Note:** This is the beginning of the default Apache welcome page. You may want to replace it for the production installation. This can be achieved by mounting a persistent volume at /var/www/html. For demo purposes, this output indicates that the application itself works and is accessible.

Creating a service
The service may be created in two different ways:

Using oc expose
From the YAML/JSON definition
We will describe both methods. You don't have to use both.

Creating a service using oc expose
You can create a pod using oc expose in the following way:


`oc get pod`{{execute}}


`oc expose pod httpd --name httpd`{{execute}}


`oc get svc`{{execute}}


The preceding command creates a service by exposing the pod, using name=httpd as a selector. You may define a custom service name via the --name option.

The same httpd application will be available from the service IP address, which is 172.30.128.131 in our case, but your output from the previous command most likely will be different:


`curl -s http://172.30.128.131:8080 | head -n4`{{execute}}


Let's delete the service to recreate it using another method, as shown in the following subsection:
`oc delete svc/httpd`{{execute}}


Creating a service from a YAML definition
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