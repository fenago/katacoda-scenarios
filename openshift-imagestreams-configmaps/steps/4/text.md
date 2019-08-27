#### Importing images
Image streams can be created by importing images from external registries in the internal registry:
`oc import-image nginx --confirm`{{execute}}

You can see from the preceding output that the Nginx image was uploaded into the internal registry at [[HOST_IP]]:5000/advanced/nginx. 
As you will also notice, its name corresponds to the image reference structure we provided earlier.

Let's delete the image stream to provide a clean slate for the next exercise:


`oc delete is/nginx`{{execute}}
imagestream "nginx" deleted

#### Creating applications directly from Docker images
Another way to create an image stream is to use the new-app command to create an application from a ready-to-use Docker image:

`oc new-app gists/lighttpd`{{execute}}

**Note:** Lighttpd is yet another web server, like Nginx or Apache. We used it in this example, because both Nginx and Apache image streams are supplied with OpenShift out-of-the-box.

This creates a number of resources, one of which is an image stream.

If you describe the newly created deployment config, you will see that it actually references the image stream, not the image itself:


`oc describe dc/lighttpd`{{execute}}
...
<output omitted>
...
  Containers:
   lighttpd:
    Image: gists/lighttpd@sha256:23c7c16d3c294e6595832dccc95c49ed56a5b34e03c8905b6db6fb8d66b8d950
...
<output omitted>
...
In the preceding example, DeploymentConfig references a Lighttpd server image in the image stream according to the following scheme:

gists/lighttpd: Image stream name
sha256: Indicates that the image identifier is generated using the SHA256 hash algorithm
23c7c16d3c294e6595832dccc95c49ed56a5b34e03c8905b6db6fb8d66b8d950: The image hash/ID itself
This is how deployment configs and replication controllers usually reference images in OpenShift.

Again, let's clean up the environment:
`oc delete all --all`{{execute}}

deploymentconfig "lighttpd" deleted
imagestream "lighttpd" deleted
pod "lighttpd-1-hqjfg" deleted
service "lighttpd" deleted