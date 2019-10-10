Now let's scale down the Pods, by editing the Operator configuration using `vim` or `nano` editor as shown below:

`kubectl edit wildflyserver clusterbench`{{execute}}

![](https://github.com/fenago/katacoda-scenarios/raw/master/learn-openshift-wildfly/clustering-wildfly-on-openshift-using-wildfly-operator/steps/6/1.JPG)

Set the **size** parameter to **1** and save the changes from the editor. Next, check that the Pods have scaled down:

`oc get pods -w`{{execute}}

![](https://github.com/fenago/katacoda-scenarios/raw/master/learn-openshift-wildfly/clustering-wildfly-on-openshift-using-wildfly-operator/steps/6/2.JPG)
