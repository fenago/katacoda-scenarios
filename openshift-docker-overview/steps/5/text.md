We told you that Docker was logging the container output.
Let's see that now.
`docker logs mycontainer`{{execute}}

- We specified a container name.
- You can, of course, specify the full ID.
- The logs command will output the entire logs of the container.

## Output
> Sat Aug  3 11:43:28 UTC 2019
> Sat Aug  3 11:43:29 UTC 2019


Executing commands inside a container
From the output, we can see that the container status is UP. Now we can execute some commands inside the container using the docker exec command with different options:


`docker exec -i backgroundcontainer ls -l /`{{execute}}
total 12
drwxr-xr-x. 2 root root 4096 Feb 15 04:18 bin
drwxr-xr-x. 2 root root 6 Nov 19 15:32 boot
drwxr-xr-x. 5 root root 360 Mar 6 21:17 dev
drwxr-xr-x. 42 root root 4096 Mar 6 21:17 etc
drwxr-xr-x. 2 root root 6 Nov 19 15:32 home
...
Output truncated for brevity
...
Option -i (--interactive) allows you to run a Docker without dropping inside the container. But we can easily override this behavior and enter this container by using -i and -t (--tty) options (or just -it):


`docker exec -it backgroundcontainer /bin/bash`{{execute}}
root@backgroundcontainer:/usr/local/apache2#
We should fall into container bash CLI. From here, we can execute other general Linux commands. This trick is very useful for troubleshooting. To exit the container console, just type exit or press Ctrl + D.

Starting and stopping containers
We can also stop and start running containers by running docker stop and docker start commands:


Enter the following command to stop the container:
`docker stop backgroundcontainer`{{execute}}

Enter the following command to start the container:
`docker start backgroundcontainer`{{execute}}