In this step, we will talk about `whoami`. We will also use this command to get token to use it with openshift rest api.

Execute `token=$(oc whoami -t)`{{execute}} to save the token.

Next, you can check if it was successful: `oc whoami`{{execute}}

Execute `oc whoami $token`{{execute}} to get the owner of the token.

Should return a response of:
``developer``



In order to create a new OpenShift project, you must use the oc new-project command:
`oc new-project new-project1`{{execute}}

This command creates a new project and automatically switches to it. In our case, it switches to new-project1. We can manually switch to another available project by running the oc project command. Let's switch to the default project:


`oc project default`{{execute}}

In order to delete an OpenShift project, you can use the oc delete command:


`oc delete project new-project1
project "new-project1" deleted
We are going to work with projects closely in the subsequent chapters. 


