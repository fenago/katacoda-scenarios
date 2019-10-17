Podman is a container runtime which provides the same features of Docker. The main difference is that it doesn’t require any running daemon (like dockerd) to run on your system. Pods and containers processes are created as children of the Podman tool. Besides it, it can also run without root privileges. So let’s see how we can use it to run some simple Linux containers and WildFly application server.

Installing Podman
The installation of podman is quite simple: all you need is using the yum/dnf tool to install the "podman" library:

```
--------- CentOS --------------
```

`sudo yum -y install podman`{{execute}}
