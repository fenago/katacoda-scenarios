Using oc new-app
The oc utility allows you to deploy a simple application in a user-friendly way. Generally, you just need to pass one or more options to the oc new-app command, which will then create all required resources, including pod(s) and service(s), for your application. Additionally, that command creates ReplicationController and DeploymentConfig API objects that control how your application is being deployed.

 
The oc new-app command
So,oc new-appcreates the following resources during application deployment from an existing Docker image:

Resource | Abbreviation | Description
--- | ---
`Pod` | *pod* | *Pod representing your container*
`Service:admin` | *svc* | *Service containing an internal application endpoint*
`ReplicationController` | *rc* | *A replication controller is an OpenShift object that controls the number of replicas for an application*
`DeploymentConfig` | *dc* | *Deployment configuration is a definition of your deployment*

 

oc new-app is a very simple utility, yet it's powerful enough to satisfy most simple deployments.

**Note:**
oc new-app doesn't create a route when deploying an application from its Docker image!

The functionality provided by oc new-app is also exposed via a web console which is what developers usually are inclined to use. 

Using oc new-app with default options

Let's delete the resources created previously:
`oc delete all --all`{{execute}}


**Note:**
Another method to delete everything is to delete the project and create it again.

Recently, we showed that OpenShift comes with an image stream that contains the path to the OpenShift-ready httpd image. The oc new-app utility uses Docker images referenced by image streams by default.

Here is an example of creating a basic httpd application:
`oc new-app httpd`{{execute}}


Run `oc status`{{execute}} to view your app.

The deployment process takes some time. Once everything is ready, you can check that all resources have been created:
`oc get all`{{execute}}

```
NAME REVISION DESIRED CURRENT TRIGGERED BY
deploymentconfigs/httpd 1 1 1 config,image(httpd:2.4)

NAME READY STATUS RESTARTS AGE
po/httpd-1-n7st4 1/1 Running 0 31s

NAME DESIRED CURRENT READY AGE
rc/httpd-1 1 1 1 32s

NAME CLUSTER-IP EXTERNAL-IP PORT(S) AGE
svc/httpd 172.30.222.179 <none> 8080/TCP,8443/TCP 33s
``` 

Let's make sure that the proper image has been used:
`oc describe pod httpd-1-n7st4 | grep Image:`{{copy}}

What is left is to expose the service to make the application externally available:

`oc expose svc httpd`{{execute}}

`curl -s http://httpd-simpleappication.127.0.0.1.nip.io | head -n 4`{{execute}}

