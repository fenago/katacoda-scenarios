We will learn now how to load in a Pod a Docker image available from Docker Hub. Let's say you want the custom image "wildfly-100-centos7":

`docker search wildfly-100-centos7`{{execute}}

```
INDEX       NAME                                             DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
docker.io   docker.io/openshift/wildfly-100-centos7          A Centos7 based WildFly v10.0 image for us...   1       
```

This is a WildFly intended for use with OpenShift which is enabled for `Source-To-Image`.

**Source-to-Image (S2I)** is a mechanism for building custom Docker images. It produces ready-to-run images by injecting application source into a Docker image and assembling a new Docker image. The new image incorporates the base image and built source