Run an instance of an **jpetazzo/clock** image in background. Also, pass ` --name=mycontainer `{{copy}} to give container custom name

### Tip:
If you are not sure, execute the `docker run --help`{{execute}} command to identify the right option to run a docker container in the **detached** mode.



The first step in running and using a container on your server or laptop is to search and pull a Docker image from the Docker registry using the docker search command.

Let's search for the web server container. The command to do so is:

Copy
$ docker search httpd
NAME DESCRIPTION STARS OFFICIAL AUTOMATED
httpd ... 1569 [OK]
hypriot/rpi-busybox-httpd ... 40
centos/httpd 15 [OK]
centos/httpd-24-centos7 ... 9
Alternatively, we can go to https://hub.docker.com/ and type httpd in the search window.


Docker Hub search results

Once the container image is found, we can pull this image from the Docker registry in order to start working with it. To pull a container image to your host, you need to use the docker pull command:

`docker pull httpd`{{execute}} 


Note that Docker uses concepts from union filesystem layers to build Docker images. This is why you can see seven layers being pulled from Docker Hub. One stacks up onto another, building a final image.

By default, Docker will try to pull the image with the latest tag, but we can also download an older, more specific version of an image we are interested in using different tags. The best way to quickly find available tags is to go to https://hub.docker.com/, search for the specific image, and click on the image details:


Docker Hub image details

There we are able to see all the image tags available for us to pull from Docker Hub. There are ways to achieve the same goal using the docker search CLI command, which we are going to cover later in this book.

`docker pull httpd:2.2.29`{{execute}} 
The output of the preceding code should look something like the following:

#### Working with images
Now we want to check the images available on our local server. To do this, we can use the docker images command:
`docker images`{{execute}} 


If we downloaded a wrong image, we can always delete it from the local server by using the docker rmi command: ReMove Image (RMI). In our case, we have two versions of the same image, so we can specify a tag for the image we want to delete:
`docker rmi httpd:2.2.29`{{execute}} 


`docker images`{{execute}} 
The output of the preceding command will be as shown in the following screenshot: