In this step, we will learn OpenShift CLI using the command _oc_.

Before we begin, make sure that your OpenShift is up and running. Run the folowing command to login to the OpenShift cluster
`oc login -u system:admin`{{execute}}

# Output

```
Login successful.

You don't have any projects. You can try to create a new project, by running

    oc new-project <projectname>
```

Openshift CLI has a lot of similarities with Kubernetes CLI. oc is short for OpenShift client, which works similarly to Kubernetes's kubectl. You will find a lot of similarities between these two commands as we go.

# Openshift Project
Openshift Project is similar to the Kubernetes namespace which also supports access controls for different users.

To complete this step, create a new project called ``myproject`` using CLI.