A service named clusterbench-loadbalancer has been created as well:
`oc get services`{{execute}}

```
NAME                        TYPE           CLUSTER-IP      EXTERNAL-IP                   PORT(S)          AGE
clusterbench-loadbalancer   LoadBalancer   172.30.26.204   172.29.128.16,172.29.128.16   8080:31886/TCP   3d
```

In order to test the application, expose the service clusterbench-loadbalancer with a Route:

`oc expose svc/clusterbench-loadbalancer`{{execute}}

```
route.route.openshift.io/clusterbench-loadbalancer exposed
```
Now let's try to access the application on the browser with:

http://clusterbench-loadbalancer-myproject.[[HOST_SUBDOMAIN]]-80-[[KATACODA_HOST]].environments.katacoda.com/clusterbench/session