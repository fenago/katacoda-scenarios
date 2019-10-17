In this tutorial we will learn how to configure JVM settings for WildFly Container running on Openshift. More in detail, we will see how to apply other JAVA_OPTS to the process and how to set the Memory settings for the JVM

`oc get pods -w`{{execute}}

Out of the box, the WildFly application server configures the JVM settings through the `JAVA_OPTS` environment variable. When moving to the Paas, this is done differently. So if you want to add a JVM argument to the WildFly process, you have to include this information in the `JAVA_OPTS_EXT` environment variable. In the following example, we are adding the attribute to the Deployment config, but it can be done on creation of the image as well:

![](https://github.com/fenago/katacoda-scenarios/raw/master/learn-openshift-wildfly/configuring-wildfly-jvm-on-openshift/steps/4/2.JPG)

**Name:** `JAVA_OPTS_EXT`{{copy}} 

**Value:** `-Dx=1`{{copy}}

![](https://github.com/fenago/katacoda-scenarios/raw/master/learn-openshift-wildfly/configuring-wildfly-jvm-on-openshift/steps/4/1.png)

Once included the environment variable, the Pod will be recreated with the included environment variable. As you can see, the environment variable "x" has been included:


![](https://github.com/fenago/katacoda-scenarios/raw/master/learn-openshift-wildfly/configuring-wildfly-jvm-on-openshift/steps/4/1.JPG)

```
JAVA_OPTS: -server -XX:+UseParallelGC -Xms40m -Xmx256m -XX:+AggressiveOpts -XX:MinHeapFreeRatio=20 -XX:MaxHeapFreeRatio=40 -XX:GCTimeRatio=4 -XX:AdaptiveSizePolicyWeight=90 -Dorg.apache.tomcat.util.LOW_MEMORY=true -DOPENSHIFT_APP_UUID= -Djboss.modules.system.pkgs=org.jboss.byteman -Djava.awt.headless=true -Dorg.jboss.resolver.warning=true -Djava.net.preferIPv4Stack=true -Dfile.encoding=UTF-8 -Djboss.node.name=demo-1-d6chu -Djgroups.bind_addr=0.0.0.0 -Dorg.apache.coyote.http11.Http11Protocol.COMPRESSION=on -Dx=1
```

