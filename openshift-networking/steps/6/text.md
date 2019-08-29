
At the beginning of this chapter, we provided diagrams detailing the DNS architecture and DNS request flow in OpenShift. Now, let's see what it looks like on a live cluster.

Run the following command on the master to see what processes are listening on TCP and UDP ports ending with 53 (DNS):
`ss -tulpn | grep '53 '`{{execute}}

```
udp UNCONN 0 0 *:8053 *:* users:(("openshift",pid=1492,fd=10))
tcp LISTEN 0 128 *:8053 *:* users:(("openshift",pid=1492,fd=13))
```
The process launched from the openshift binary is no other than the OpenShift Master API, as SkyDNS is embedded into it and uses etcd as a source of authority to keep track of new services and to delete records for deleted ones:

`ps auxf | grep openshift`{{execute}}

Now, let's take a look at listening ports on our first node—the setup is completely the same for all nodes in a cluster:


`ss -tulpn | grep '53 '`{{execute}}
