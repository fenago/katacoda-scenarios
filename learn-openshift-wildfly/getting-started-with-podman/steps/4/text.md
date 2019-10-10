

We can check the virtual IP Address that has been assigned to your container and reach it out:
`podman inspect wildfly | grep "IPAddress"`{{execute}}

Update the container ip and run following command:
`curl <container-ip>:8080 | grep "WildFly"`{{copy}}