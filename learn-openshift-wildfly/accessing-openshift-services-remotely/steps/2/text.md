In this article we will learn how to connect to services running in Openshift Paas from external clients

Out of the box Openshift uses the router component to let external clients access the services running in the Paas. The router is however limited to HTTP/HTTPS(SNI)/TLS(SNI), which covers web applications. In this article we will see how to access some services from remote clients using the simple mechanism provided by the oc port-forward command.


#### Openshift Templates

Now we will add an application out of the available templates:
Once ready, open a terminal and at the command prompt, enter the following command to create a Java web application.

`oc get templates -n openshift`{{execute T1}}

For our example, we will create a mysql database, and let the template assign some defaults:
`oc new-app mysql-ephemeral --name=mysqldemo`{{execute T1}}


#### Output
And the output should look something like this:

```

--> Deploying template "openshift/mysql-ephemeral" to project myproject
 
     MySQL (Ephemeral)
     ---------
     MySQL database service, without persistent storage. For more information about using this template, including OpenShift considerations, see https://github.com/sclorg/mysql-container/blob/master/5.6/README.md.
 
WARNING: Any data stored will be lost upon pod destruction. Only use this template for testing
 
     The following service(s) have been created in your project: mysql.
 
       Username: user3XH
       Password: CBDXVWcW3VFCV5aI
  Database Name: sampledb
 Connection URL: mysql://mysql:3306/
 
For more information about using this template, including OpenShift considerations, see https://github.com/sclorg/mysql-container/blob/master/5.6/README.md.
 
     * With parameters:
        * Memory Limit=512Mi
        * Namespace=openshift
        * Database Service Name=mysql
        * MySQL Connection Username=user3XH # generated
        * MySQL Connection Password=CBDXVWcW3VFCV5aI # generated
        * MySQL Database Name=sampledb
        * Version of MySQL Image=5.6
 
--> Creating resources ...
    service "mysql" created
    deploymentconfig "mysql" created
--> Success
    Run 'oc status' to view your app.
```

