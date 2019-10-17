The build process takes some time. During the first phase, you can see a container with -build in its name. This container is deployed from the WildFly builder image and is responsible for build operations:
`oc get pod`{{execute}}


**Note:** Please wait for the deployment to complete and all the pods to be running, It will take around **4-5 minutes** to complete.


After some time, the application will be available. That means that the application's pod should be in a Running state:
`oc get pod`{{execute}}

```
NAME              READY  STATUS     RESTARTS  AGE
myapp-1-build   0/1    Completed  0         39s
myapp-1-h9xt5   1/1    Running    0         4s
```
