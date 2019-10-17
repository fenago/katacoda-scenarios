Next thing we want to configure is the amount of memory to allocate for the JVM. As a matter of fact, including the -Xms and -Xmx option as environment variable won't work as the amount of memory to be used for the process depends on the Resource Limits assigned to the Container.

Resource limits can be configured when you create the Container from the Template or as well through the **Deployment Configuration** -> **Edit Resource Limits** as shown by the following picture:

![](https://github.com/fenago/katacoda-scenarios/raw/master/learn-openshift-wildfly/configuring-wildfly-jvm-on-openshift/steps/5/2.JPG)

![](https://github.com/fenago/katacoda-scenarios/raw/master/learn-openshift-wildfly/configuring-wildfly-jvm-on-openshift/steps/5/1.png)
