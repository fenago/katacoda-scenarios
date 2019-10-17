Running following command to list all the resources created in the project:
``oc get all -o name``{{execute}}

# Task
To complete this step, delete resources for the application by using the `--selector` parameter.

``oc delete all --selector app=<app-name>``{{copy}}

You can verify that the resources have been deleted by: ``oc get all -o name``{{execute}}