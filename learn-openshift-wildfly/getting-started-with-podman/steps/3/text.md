Now let's move into wildfly land. You might wonder how WildFly runs with Podman: we have just checked it: it's pretty simple just replace the docker command line with podman:

`podman run -d -p 8080:8080 docker.io/jboss/wildfly`{{execute}}

![](https://github.com/fenago/katacoda-scenarios/raw/master/learn-openshift-wildfly/getting-started-with-podman/steps/3/1.png)

As you can see from the above picture, we have used 'podman ps' to track the running container processes. If you tried to run the same command with docker CLI, it would return an empty list, as containers are not running via Docker!

`podman ps`{{execute}}
