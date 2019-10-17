Besides running containers, you can use Podman also to interact with container registries like docker.io. To do that, simply log in to a container registry like Docker Hub:

`podman login docker.io`{{execute}}

Now you can push the images you have built, taking care to tag it so it refers to the specific container registry and my personal namespace, and then simply push it.

`podman -t mywildfly docker.io/user/mywildfly`{{copy}}

`podman push docker.io/user/mywildfly`{{copy}}