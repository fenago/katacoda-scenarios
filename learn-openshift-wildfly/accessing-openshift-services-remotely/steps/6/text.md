Let's see another example so that we can connect to Wildfly application server CLI or Web console. Let's create the application at first:

`oc new-app jboss/wildfly --name=wildfly`{{execute T1}}

```
--> Found Docker image d59073d (11 days old) from Docker Hub for "jboss/wildfly"
 
    * An image stream will be created as "wildfly:latest" that will track this image
    * This image will be deployed in deployment config "wildfly"
    * Port 8080/tcp will be load balanced by service "wildfly"
      * Other containers can access this service through the hostname "wildfly"
 
--> Creating resources ...
    imagestream "wildfly" created
    deploymentconfig "wildfly" created
    service "wildfly" created
--> Success
    Run 'oc status' to view your app.
```

#### Expose Application
Let's check that the service is available:
`oc get services`{{execute T1}}

Let's expose the route for this service:
`oc expose service wildfly`{{execute T1}}

```
route "wildfly" exposed
```
