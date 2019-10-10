

We can check the virtual IP Address that has been assigned to your container and reach it out:
`podman inspect <container-id> | grep "IPAddress"`{{copy}}

Update the container ip and run following command:
`curl <container-ip>:8080 | grep "WildFly"`{{copy}}

![](https://github.com/fenago/katacoda-scenarios/raw/master/learn-openshift-wildfly/getting-started-with-podman/steps/4/1.png)