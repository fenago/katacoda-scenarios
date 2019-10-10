The great thing is that you can do all this with a single command. So let's say you want to load the image "openshift/wildfly-100-centos7" and produce a new image using the source code available on https://github.com/fmarchioni/mastertheboss in the folder "openshift-demo"

(Have a look at the application here: https://github.com/fmarchioni/mastertheboss/tree/master/os-demo)

Here's the command which does the magic:

`oc new-app openshift/wildfly-100-centos7~https://github.com/fmarchioni/mastertheboss   --context-dir=os-demo --name=demo-wildfly`{{execute}}

As you can see from the output several things happen:

- The image is searched in DockerHub. It's found and then loaded
- An image stream will be created for it that will track the source image
- A source build using source code from https://github.com/fmarchioni/mastertheboss will be created
- This image will be deployed in deployment config "demo-wildfly"


![](https://github.com/fenago/katacoda-scenarios/raw/master/learn-openshift-wildfly/deploy-docker-images-on-openshift/steps/4/1.JPG)