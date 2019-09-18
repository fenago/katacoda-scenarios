Take a look at the Dockerfile in the root folder of the project. This file describes the environment that is required to run the function app on Linux. The following example is a Dockerfile that creates a container that runs a function app on the JavaScript (Node.js) worker runtime:

#### Dockerfile

```
FROM mcr.microsoft.com/azure-functions/node:2.0

ENV AzureWebJobsScriptRoot=/home/site/wwwroot
COPY . /home/site/wwwroot
```

#### Run the build command
In the root folder, run the docker build command, and provide a name, mydockerimage, and tag, v1.0.0. Replace <docker-id> with your [Docker Hub](https://hub.docker.com)account ID. This command builds the Docker image for the container.
`docker build --tag <docker-id>/mydockerimage:v1.0.0 .`{{copy}}

When the command executes, you see something like the following output, which in this case is for a Typescript worker runtime:

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-azure-cli/steps/7/1.JPG)
