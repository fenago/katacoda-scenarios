And here is the service which is now available:
`oc get svc`{{execute}}

```
NAME           CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
demo-wildfly   172.30.182.135   <none>        8080/TCP   34s
```

In order to enable using the service to external clients, we will create a route which will expose the http port 8080 of the service:
`oc expose svc demo-wildfly`{{execute}}

As you can see, now the demo application is exposed through a router:

`oc get routes`{{execute}}

```
NAME           HOST/PORT                                    PATH      SERVICES       PORT       TERMINATION
demo-wildfly   demo-wildfly-myproject.192.168.1.66.xip.io             demo-wildfly   8080-tcp   
```

If you prefer you can browse through the console and click on the router to test the application!