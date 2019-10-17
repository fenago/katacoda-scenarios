Now that the ImageStream is available, let's create an application in the current project which uses this ImageStream:

`oc new-app --image-stream=mywildfly`{{execute}}

```
--> Found image 57af1ff (48 seconds old) in image stream "myproject/mywildfly" under tag "latest" for "mywildfly"
 
    * This image will be deployed in deployment config "mywildfly"
    * Port 8080/tcp will be load balanced by service "mywildfly"
      * Other containers can access this service through the hostname "mywildfly"
 
--> Creating resources ...
    deploymentconfig.apps.openshift.io "mywildfly" created
    service "mywildfly" created
--> Success
    Application is not exposed. You can expose services to the outside world by executing one or more of the commands below:
     'oc expose svc/mywildfly'
    Run 'oc status' to view your app.
```

Please wait for the deployment to complete and all the pods to be running, It will take around **2 minutes** to complete.
`oc get pods`{{execute}}
