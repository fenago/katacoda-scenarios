Just like with the standard UNIX command tail -f, we can follow the logs of our
container:

`docker logs --tail 1 --follow mycontainer`{{execute}}

## Output
> Sat Aug  3 11:43:28 UTC 2019
> Sat Aug  3 11:43:29 UTC 2019

- This will display the last line in the log file.
- Then, it will continue to display the logs in real time.
- Use ^C to exit.


In order to delete a container, you can use the docker rm command. If the container you want to delete is running, you can stop and delete it or use the -f option and it will do the job:


`docker rm 3b1150b50343`{{execute}}

```
Error response from daemon: You cannot remove a running container 3b1150b5034329cd9e70f90ee21531b8b1ab1d4a85141fd3a362cd40db80e193. 
```

Stop the container before attempting removal or force remove. Let's try using -f option.
`docker rm  -f 3b1150b50343`{{execute}}

Another trick you can use to delete all containers, both stopped and running, is the following command:
`docker rm -f $(docker ps -qa)`{{execute}}


```
830a42f2e727
backgroundcontainer
mycontainer
419e7ce2567e
```

Verify that all the containers are deleted:
`docker ps  -a`{{execute}}