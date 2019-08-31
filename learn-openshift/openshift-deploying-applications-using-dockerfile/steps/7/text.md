Now we can check the version of our application:
`oc rsh redis-2-l6bbl /usr/local/bin/redis-server --version`{{execute}}

```
Redis server v=4.0.9 sha=00000000:0 malloc=jemalloc-4.0.3 bits=64 build=40ca48d6a92db598
```

Finally, let's make sure that the application is up and running:
`oc rsh redis-2-l6bbl /usr/local/bin/redis-cli ping`{{execute}}

We were able to initiate the build from the updated source code.

Clear out your lab environment.
`oc delete all --all`{{execute}}

`oc delete project dockerfile`{{execute}}
