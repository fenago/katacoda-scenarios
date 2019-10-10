That's it! you can check from the local jboss-cli that you are able to connect with the credentials provided:

`./jboss-cli.sh -c`{{execute}}

**Username:** `admin`{{execute}}

**Password:** `admin123`{{execute}}

```
Authenticating against security realm: ManagementRealm
Username: admin
Password: 
[standalone@localhost:9990 /] 
```

Much the same way, you can connect to the Web console as you can see from the following picture:

https://[[HOST_SUBDOMAIN]]-9990-[[KATACODA_HOST]].environments.katacoda.com/

![](https://github.com/fenago/katacoda-scenarios/raw/master/learn-openshift-wildfly/accessing-openshift-services-remotely/steps/9/1.png)
