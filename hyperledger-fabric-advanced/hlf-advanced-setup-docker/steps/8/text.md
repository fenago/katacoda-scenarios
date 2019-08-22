
**Note:** Run following commands from the new terminal. Open it by clicking add icon and click `Open New Terminal`.

Let's push our image to docker hub. You need to have docker hub account for this.
`docker login`{{execute}}

#### Image Tag
Let's tag our image using docker tag command which will create a tag TARGET_IMAGE that refers to SOURCE_IMAGE.
`docker tag hlf-custom <username>/hlf-custom:latest`{{copy}} 

You can verify tag was created successfully by running `docker images`{{execute}} command.

#### Image Push
You can push image to docker hub by running following command:
`docker push <username>/hlf-custom:latest`{{execute}} 