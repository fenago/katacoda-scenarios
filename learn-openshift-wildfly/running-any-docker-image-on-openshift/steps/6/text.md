We are almost done. We only need to expose the Route to external clients:

`oc expose svc/mywildfly`{{execute}} 

```
route.route.openshift.io/mywildfly exposed
```

And verify the Route URL with:

`oc get route`{{execute}} 

```
NAME                HOST/PORT                                         PATH      SERVICES            PORT       TERMINATION   WILDCARD
mywildfly           mywildfly-myapp.192.168.42.5.nip.io                     mywildfly           8080-tcp                 None
```

As you can see, the application is available:

http://mywildfly-myapp.[[HOST_SUBDOMAIN]]-80-[[KATACODA_HOST]].environments.katacoda.com