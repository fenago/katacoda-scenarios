Next thing will be creating a Binary Build that will hold our Image. You can do it through the "oc new-build" command:

`oc new-build --binary --name=mywildfly -l app=mywildfly`{{execute}}

![](https://github.com/fenago/katacoda-scenarios/raw/master/learn-openshift-wildfly/running-any-docker-image-on-openshift/steps/3/1.JPG)

Great. Now verify that the Binary Build has been correctly added:

`oc get bc`{{execute}}

```
NAME                TYPE      FROM      LATEST
mywildfly           Docker    Binary    0
```

As it is, the Binary Build does not contain any reference to a Dockerfile. We can edit its configuration to include, in the dockerfilePath param, the location where our Dockerfile is (in our case, it's in the current folder):

`oc patch bc/mywildfly -p '{"spec":{"strategy":{"dockerStrategy":{"dockerfilePath":"Dockerfile"}}}}'`{{execute}}

```
buildconfig.build.openshift.io/mywildfly patched
```
