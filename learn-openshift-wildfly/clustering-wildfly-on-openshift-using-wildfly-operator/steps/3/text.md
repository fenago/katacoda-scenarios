To install a WildFly cluster, we will need to provide the HA XML configuration as a ConfigMap that is accessible by the Operator. Let's see how to do it. First of all, some grants are required, so provide to your user the service account Role for your project with:

`oc policy add-role-to-user view system:serviceaccount:$(oc project -q):default -n $(oc project -q)`{{execute}}

```
role "view" added: "system:serviceaccount:myproject:default"
```

#### Git Clone
Clone the following repository by executing following command in the terminal.
`git clone https://github.com/athertahir/openshift-wildfly.git`{{execute}}

Now, move in the directory which contains the yaml files.

`cd openshift-wildfly/wildfly-operator/`{{execute}}

In the next step, we will use the example configuration from GitHub: https://github.com/athertahir/openshift-wildfly/tree/master/wildfly-operator

