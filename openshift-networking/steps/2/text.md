Move on to creating the second project:
`oc new-project demo-2`{{execute}}

And create the same pod in that project:
`oc create -f httpd-pod.yml`{{execute}}

Now, let's see whether we can ping the first pod from the one we have just created:

`oc rsh httpd ping 10.129.0.22`{{copy}}

```
PING 10.129.0.22 (10.129.0.22) 56(84) bytes of data.
64 bytes from 10.129.0.22: icmp_seq=1 ttl=64 time=0.345 ms
...
<output omitted>
...
```

As you can see, communication between pods is completely uninhibited, which may be undesirable. In the two following subsections, we will demonstrate how to enforce project isolation using other OpenShift plugins.
