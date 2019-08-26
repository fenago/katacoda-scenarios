How can we check that our container is still running?..

With docker ps, just like the UNIX ps command, lists running processes.
`docker ps`{{execute}}

Docker tells us:
- The (truncated) ID of our container.
- The image used to start the container.
- That our container has been running (Up) for a couple of minutes.


## Useful Commands
- Use the -l ("Last") to list last container that was started `docker ps -l`{{execute}}
- Use the -q ("Quiet", "Quick") to list only the IDs of our containers `docker ps -q`{{execute}}
- We can combine -l and -q to see only the ID of the last container started: `docker ps -lq`{{execute}}




The Docker CLI allows us to export and import Docker images and container layers using export/import or save/load Docker commands. The difference between save/load and export/import is that the first one works with images including metadata, but the export/import combination uses only container layers and doesn't include any image metadata information such as name, tags, and so on. In most cases, the save/load combination is more relevant and works properly for images without special needs. The docker save command packs the layers and metadata of all the chains required to build the image. You can then load this saved images chain into another Docker instance and create containers from these images.

The docker export will fetch the whole container, like a snapshot of a regular VM. It saves the OS, of course, but also any change a you made and any data file written during the container life. This one is more like a traditional backup:

Copy
`docker save httpd -o httpd.tar`{{execute}}

`ls -l httpd.tar`{{execute}}

To load the image back from the file, we can use the docker load command. Before we do that, though, let's remove the httpd image from the local repository first:

Copy
`docker rmi httpd:latest
The output of the preceding command will be as shown in the following screenshot:


We verify that we do not have any images in the local repository:

 `docker images`{{execute}}

Load the image file we previously saved with the docker save command. Like docker export and docker import, this command forms a pair with Docker save and thus is used for loading a saved container archive with all intermediate layers and metadata to the Docker cache:

Copy
`docker load -i httpd.tar`{{execute}}
The output of the preceding command will be as shown in the following screenshot:


Check the local docker images with docker image command:
`docker images`{{execute}}


Uploading images to the Docker registry
Now we know how to search, pull, remove, save, load, and list available images. The last piece we are missing is how to push images back to Docker Hub or a private registry.