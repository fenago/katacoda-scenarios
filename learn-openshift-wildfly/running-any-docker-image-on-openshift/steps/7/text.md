As last step, we will be accessing application using cURL. For this purpose we need to define a PortForward to reach the port 8080 in the Pod where the Application us running. Let's check the Pod list:

`oc get pods`{{execute}}

**Note:** Please wait for few seconds to see pods status running.

![](https://github.com/fenago/katacoda-scenarios/raw/master/learn-openshift-wildfly/running-any-docker-image-on-openshift/steps/7/1.JPG)

Now we will forward the Port 8080 to the equivalent Port on localhost:

`oc port-forward mywildfly-1-<update> 8080:8080`{{copy}}

**Important:** Run above command in **terminal 2** . You can open it by clicking `+` icon and selecting `new terminal`

```
Forwarding from 127.0.0.1:8080 -> 8080
Forwarding from [::1]:8080 -> 8080
```

Try accessing application using cURL at port `8080`

`curl localhost:8080`{{execute}}

**Protip:** Press `Ctrl` + `C` keys in **terminal 2** to close the connection with wildfly and run `curl localhost:8080`{{execute}} command again. It will fail to get response.