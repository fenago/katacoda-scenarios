Now start the Build:

`oc start-build mywildfly --from-dir=. --follow`{{execute}}

The build of our application is now scheduled, and it will take **up to 4-5 minutes** before it's complete.

![](https://github.com/fenago/katacoda-scenarios/raw/master/learn-openshift-wildfly/running-any-docker-image-on-openshift/steps/4/1.JPG)


Well done, the ImageStream has been pushed into the Internal Registry. Check it with:

`oc get is`{{execute}}

```
NAME                DOCKER REPO                                   TAGS      UPDATED
mywildfly           172.30.1.1:5000/myproject/mywildfly           latest    12 seconds ago
```
