In this scenario, we will add custom modules and deployments to WildFly on Openshift. It is available on [github](https://github.com/fmarchioni/mastertheboss/tree/master/openshift/module), will show how to add external modules and deployments during the Source to Image process.

![](https://github.com/fenago/katacoda-scenarios/raw/master/learn-openshift-wildfly/customize-wildfly-applications-on-openshift/steps/2/1.png)

As you can see from the above picture, you can use the following folders:

- **modules:** Place here modules just like you would do in a bare-metal installation of WildFly. They will be automatically uploaded on WildFly
- **deployments:** Place here artifacts that are to be deployed on the application server.

![](https://github.com/fenago/katacoda-scenarios/raw/master/learn-openshift-wildfly/customize-wildfly-applications-on-openshift/steps/2/2.JPG)

The module.xml loads the itext JAR file and uploads it into the application server.

```
<module xmlns="urn:jboss:module:1.1" name="com.itext">
 
    <properties>
        <property name="jboss.api" value="private"/>
    </properties>
 
      <resources>
        <resource-root path="itext-5.0.5.jar"/> 
    </resources>
 
</module>
```

In order to link the library with the application server add a jboss-deployment-structure.xml file:

```
<jboss-deployment-structure>
  <deployment>
    <dependencies>
      <module name="com.itext" />
    </dependencies>
    </deployment>
</jboss-deployment-structure>
```

