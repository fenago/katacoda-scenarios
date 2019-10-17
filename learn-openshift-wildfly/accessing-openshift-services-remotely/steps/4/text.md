 We have created a route, however even with a route connection to the container is still limited to http. Thus, it is necessary to port-forward the route to localhost using the oc tool. Let's see the pod name:

`oc get pods`{{execute T1}}

Copy pod name and let's forward this pod through the port `3306` as follows:

**Important:** Run command below in **terminal 2** . You can open it by clicking `+` icon and selecting `new terminal`

`oc port-forward mysql-1-<update> 3306:3306`{{copy}}

```
Forwarding from 127.0.0.1:3306 -> 3306
Forwarding from [::1]:3306 -> 3306
Handling connection for 3306
```
