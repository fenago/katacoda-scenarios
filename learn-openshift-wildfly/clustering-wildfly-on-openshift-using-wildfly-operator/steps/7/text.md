Let's try to access again the application on the browser with:

http://clusterbench-loadbalancer-myproject.[[HOST_SUBDOMAIN]]-80-[[KATACODA_HOST]].environments.katacoda.com/clusterbench/session



As you can see, the session counter keeps increasing, even if we scaled down the number of Pods.

Great! We just managed to set up a basic example of WildFly cluster on Openshift using WildFly Operator. 