Take note of **user**, **password** and database name from `new-app` command output and let's move on. The mysql service should be available:

`oc get services`{{execute T1}}

```
NAME      CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
mysql     172.30.232.104   <none>        3306/TCP   1m
```

#### Create Route
Let's expose this service through a route:

`oc expose service mysql`{{execute T1}}

```
route "mysql" exposed
```

