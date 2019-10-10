Running following command to list all the resources created in the project:
``oc get all -o name``{{execute}}

This will display output similar to:

```
pod/demo-1-build
service/demo
deploymentconfig.apps.openshift.io/demo
buildconfig.build.openshift.io/demo
build.build.openshift.io/demo-1
imagestream.image.openshift.io/demo
route.route.openshift.io/demo
```

# Task
To complete this step, delete resources for the application by using the `--selector` parameter.

You can verify that the resources have been deleted by: ``oc get all -o name``{{execute}}