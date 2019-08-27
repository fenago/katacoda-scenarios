
Tracking the version history of images using ImageStreams
Certain OpenShift resources, such as pods, deployments, DeploymentConfigs, ReplicationControllers, and ReplicaSets reference Docker images for deploying containers. Instead of referencing images directly, the common approach is to reference them through image streams, which serve as a layer of indirection between the internal/external repository and client resources, creating a virtual view of available images.

Note
In the official documentation and some blogs, you may come across comparing image streams to repositories. While it's true in the sense that resources reference images in image streams just like in repositories, this analogy lacks clarity; image streams don't store anything by themselves and are only abstractions for image management. So, in this chapter, we will talk of them as virtual views to give you a more accurate idea of what they actually are.

Using image streams has the following advantages:

Your application won't break unexpectedly if the upstream image's update introduced errors, because the image stream tags your pod points so that it will still be mapped to the working version of the image, effectively protecting you from outages
Image-change triggers and periodic reimports of the image can be configured at the image stream's level
You more than likely won't have to create ImageStreams from scratch, but it's important to understand their structure in order to understand their functions.

OpenShift include default image streams for some of the most popular images, such as PostgreSQL, HTTPD, and Python. They reside in the openshift project:
`oc get is -n openshift`{{execute}}


In order to see what the words indirection layer from the beginning of this section mean, let's take a closer look at the mongodb image stream:
`oc describe is/mongodb -n openshift`{{execute}}

...
<output omitted>
...
Unique Images:   3
Tags:            4

3.2 (latest)
  tagged from centos/mongodb-32-centos7:latest

  Provides a MongoDB 3.2 database on CentOS 7. For more information about using this database image, including OpenShift considerations, see https://github.com/sclorg/mongodb-container/tree/master/3.2/README.md.
  Tags: mongodb

  * centos/mongodb-32-centos7@sha256:d4dc006a25db1423caed1dcf0f253f352dbbe0914c20949a6302ccda55af72b1
      22 hours ago
...
<output omitted>
...
Image streams use a particular notation to reference images in repositories. Let's take a reference from the preceding example and break it down:



ImageStreams are not useful by themselves and only exist to support the life cycle of applications. They are usually created behind the scenes in the following scenarios:

- Creating applications from S2I builds
- Importing images
- Creating applications directly from Docker images
- Manually pushing images into the internal registry

Since S2I builds will be discussed further in this book, we will consider three other methods.
