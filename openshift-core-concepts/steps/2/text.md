In this step, you will learn to use openshift web console.

## Task 1
You can access the `Openshift Web Console` by clicking `Dashboard` tab located right to the terminal window. This tab is connected to Port `8443` of the docker host which is hosting openshift web console.

**Username:** ``developer``{{}}
**Password:** ``developer``{{}}

After logging in to the web console, you'll see a project we created in the previous step. Select ``myproject`` and you should be able to see  _Overview_ page.

## Task 2
After selecting project, you will see **Add to Project** next to the name of your project, in this case **myproject**. 

Explore web console by selecting verious resources like **Builds >**, **Applications >** and **Resources >**.


OpenShift project is a Kubernetes namespace with additional features called annotations that provide user multi-tenancy and role-based access control in OpenShift. Each project has its own set of policies, constraints, and service accounts. You can see that the number of namespaces and projects in OpenShift is the same. The commands we are going to need are oc get namespaces and oc get projects:


`oc get projects`{{execute}}
NAME DISPLAY NAME STATUS
default Active
kube-public Active
kube-system Active
myproject My Project Active
openshift Active
openshift-infra Active
openshift-node Active

`oc get namespaces`{{execute}}
NAME              STATUS    AGE
default           Active     3d
kube-public       Active     3d
kube-system       Active     3d
myproject         Active     3d
openshift         Active     3d
openshift-infra   Active     3d
openshift-node    Active     3d
As we mentioned previously, each namespace, or rather project, is separated from another by a set of rules. This allows different teams to work independently from each other. In order to identify what project we are currently working in, you can use the oc projects command. This command gives you a list of OpenShift projects available for you, and it also tells you what projects you are currently working on:


`oc projects`{{execute}}

You have access to the following projects and can switch between them with 'oc project <projectname>':
    default
    kube-public
    kube-system
    myproject - My Project
  * new-project1
    openshift
    openshift-infra
    openshift-node
Using project "new-project1" on server "https://127.0.0.1:8443".
Note
The asterisk * also specifies the current project.We can see that there are a lot of different projects available, though we have not created any because the system admin user has access to everything. 