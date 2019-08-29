The previous command initiated a build. OpenShift starts a -build pod which does the build. You may temporarily see that a Pod with -build in the name is in the Running state:


`oc get pod`{{execute}}

```
NAME            READY    STATUS             RESTARTS    AGE
redis-1-build   1/1      Running            0           6s
redis-1-deploy  0/1      ContainerCreating  0           1s
```

Docker build is controlled by a build config object. Build status can be displayed by using the oc logs bc/<NAME> command:
`oc logs bc/redis|tail -n10`{{execute}}


OpenShift built the Redis image from Dockerfile and uploaded it to a local registry. Let's make sure that container works:
`oc get pod`{{execute}}

```
NAME             READY    STATUS      RESTARTS  AGE
redis-1-build    0/1      Completed   0         2m
redis-1-js789    1/1      Running     0         1m
```

`oc exec <redis-pod-name> /usr/local/bin/redis-cli ping`{{execute}}

```
PONG
```