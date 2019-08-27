

Now, we have to simulate a large number of user requests to our pods to increase the CPU load so that autoscaling takes effect. But to do that, we need to create a route first:
`oc expose svc/httpd`{{execute}}

`oc get route`{{execute}}
... httpd-advanced.openshift.example.com ...
At this point, we have everything we need, so let's start simulating CPU load with the ab Apache benchmarking utility:

`yum install httpd-tools`{{execute}}

`ab -c 100 -n 10000000 -H 'Host: httpd-advanced.openshift.example.com' http://127.0.0.1/`{{execute}}

```
...
<output omitted>
...
^C
Percentage of the requests served within a certain time (ms)
  50% 46
  66% 56
  75% 66
  80% 73
  90% 95
  95% 124
  98% 171
  99% 200
 100% 528 (longest request)
```


When httpd DeploymentConfig is scaled up, you can just press Ctrl+C to stop generating the traffic, as is indicated by ^C in the output above.
