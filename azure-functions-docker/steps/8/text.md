Verify that the image you built works by running the Docker image in a local container. Issue the docker run command and pass the name and tag of the image to it. Be sure to specify the port using the -p argument.

`docker run -p 8080:80 -it <docker-ID>/mydockerimage:v1.0.0`{{copy}}

With the custom image running in a local Docker container, verify the function app and container are functioning correctly by clicking `Docker Azure` tab located next to terminal icon.

After you have verified the function app in the container, stop the execution. Now, you can push the custom image to your Docker Hub account.

