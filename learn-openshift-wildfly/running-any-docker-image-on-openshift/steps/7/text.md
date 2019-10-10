As last step, we will verify that we can actually login with the management user that has been incldued in the Image. For this purpose we need to define a PortForward to reach the port 9990 in the Pod where the Application us running. Let's check the Pod list:

`oc get pods`{{execute}}


![](https://github.com/fenago/katacoda-scenarios/raw/master/learn-openshift-wildfly/running-any-docker-image-on-openshift/steps/7/1.JPG)

Now we will forward the Port 9990 to the equivalent Port on localhost:

`oc port-forward mywildfly-1-<update> 9990:9990`{{copy}}

**Important:** Run above command in **terminal 2** . You can open it by clicking `+` icon and selecting `new terminal`

```
Forwarding from 127.0.0.1:9990 -> 9990
Forwarding from [::1]:9990 -> 9990
```

Try connecting using web console, you will be prompted to enter Username and Password.

https://[[HOST_SUBDOMAIN]]-9990-[[KATACODA_HOST]].environments.katacoda.com/console