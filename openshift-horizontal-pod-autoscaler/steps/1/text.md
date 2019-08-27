Before we begin, make sure that your OpenShift is up and running. Run the folowing command to login to the OpenShift cluster
`oc login -u system:admin`{{execute}}

# Output

```
Login successful.

You don't have any projects. You can try to create a new project, by running

    oc new-project <projectname>
```

**Note:** Please wait for the setup to complete, It will take around 2 minutes to complete.

In this scenario, we will Autoscaling our application depending on CPU and RAM utilization using openshift pod autoscaler.
