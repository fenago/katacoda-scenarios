We can also open a browser or use the curl command to verify the Kubernetes API:
`curl https://[[HOST_IP]]:8443`{{execute}}

```
{
"kind": "Status",
"apiVersion": "v1",
"metadata": {
},
"status": "Failure",
"message": "Unauthorized",
"reason": "Unauthorized",
"code": 401
}
```
#### Kubernetes GUI 
There is a nice dashboard that comes with Kubernetes's nice-looking GUI, available on port 30000 via HTTP (for example, http://[[HOST_IP]]:30000/). You can open your browser using the same IP we used for cluster verification:

http://[[HOST_SUBDOMAIN]]-30000-[[KATACODA_HOST]].environments.katacoda.com/

At this moment, there is not much to look at, as our simple cluster has only one node, one service, and three default namespaces. This is one way to manage Kubernetes, but to be able to effectively use all its features and troubleshoot issues, you need to get comfortable with using CLI, which is what the next section is about.