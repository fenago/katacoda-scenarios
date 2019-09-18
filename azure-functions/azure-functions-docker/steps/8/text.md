Verify that the image you built works by running the Docker image in a local container. Issue the docker run command and pass the name and tag of the image to it. Be sure to specify the port using the -p argument.

`docker run -p 8080:80 -it <docker-ID>/mydockerimage:v1.0.0`{{copy}}

You can also run following command if you built image without docker username in the previous step.

`docker run -p 8080:80 -it mydockerimage:v1.0.0`{{execute}}

With the custom image running in a local Docker container, verify the function app and container are functioning correctly by clicking `Docker Azure` tab located next to terminal icon.

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-docker/steps/8/1.JPG)

After you have verified the function app in the container, stop the execution by pressing `Ctrl` + `C`. Now, you can push the custom image to your Docker Hub account.

