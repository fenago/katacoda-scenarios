A registry is an application that hosts images and provides services image and container services. To share your image, you must push it to a registry. Docker Hub is a registry for Docker images that allows you to host your own repositories, either public or private.

Before you can push an image, you must sign in to Docker Hub using the docker login command. Replace `<docker-id>` with your account name and type in your **password** into the console at the prompt.

`docker login --username <docker-id>`{{copy}}

**"login succeeded"** message confirms that you're logged in. After you have signed in, you push the image to Docker Hub by using the docker push command.

`docker push <docker-id>/mydockerimage:v1.0.0`{{copy}}

Verify that the push succeeded by examining the command's output.

```
The push refers to a repository [docker.io/<docker-id>/mydockerimage:v1.0.0]
24d81eb139bf: Pushed
fd9e998161c9: Mounted from <docker-id>/mydockerimage
e7796c35add2: Mounted from <docker-id>/mydockerimage
ae9a05b85848: Mounted from <docker-id>/mydockerimage
45c86e20670d: Mounted from <docker-id>/mydockerimage
v1.0.0: digest: sha256:be080d80770df71234eb893fbe4d... size: 1796

```

Now, you can use this image as the deployment source for a new function app in Azure.
