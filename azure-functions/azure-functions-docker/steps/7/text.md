Take a look at the Dockerfile in the root folder of the project. This file describes the environment that is required to run the function app on Linux. The following example is a Dockerfile that creates a container that runs a function app on the JavaScript (Node.js) worker runtime:

#### Dockerfile

```
FROM mcr.microsoft.com/azure-functions/node:2.0

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true

COPY . /home/site/wwwroot

RUN cd /home/site/wwwroot && \
    npm install
```

**Note:** You can have a look at the `Dockerfile` content by running `cat Dockerfile`{{execute}} 

#### Run the build command
In the root folder, run the docker build command, and provide a name, `mydockerimage`, and tag `v1.0.0`. Replace <docker-id> with your [Docker Hub](https://hub.docker.com) account ID. This command builds the Docker image for the container.
`docker build --tag <docker-id>/mydockerimage:v1.0.0 .`{{copy}}

**Protip**: You can also build image without docker username, if you don't plan to push it to docker hub.
`docker build --tag mydockerimage:v1.0.0 .`{{execute}}

When the command executes, you see something like the following output, which in this case is for a Typescript worker runtime:

![](https://github.com/fenago/katacoda-scenarios/raw/master/azure-functions/azure-functions-docker/steps/7/1.JPG)
