Ok, now before port-forwarding, we will create a management user, by executing the add-user command remotely on the pod:

`oc get pods`{{execute T1}}

```
NAME              READY     STATUS    RESTARTS   AGE
wildfly-1-5sgcj   1/1       Running   0          1m
```

**Note:** Please wait for few seconds to see pods status running.

`oc exec -it wildfly-1-<update> -- /bin/bash -c "/opt/jboss/wildfly/bin/add-user.sh -m -u admin -p admin123"`{{copy}}

#### Output

```
Added user 'admin' to file '/opt/jboss/wildfly/standalone/configuration/mgmt-users.properties'
Added user 'admin' to file '/opt/jboss/wildfly/domain/configuration/mgmt-users.properties'
```

Ok, last step will be port-forwarding the port 9990 which is used both by the CLI and the Web console:

`oc port-forward wildfly-1-<update> 9990:9990`{{copy}}

**Important:** Run above command in **terminal 2** . You can open it by clicking `+` icon and selecting `new terminal`
