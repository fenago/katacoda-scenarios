We will run Jupyter Notebook as a Docker container. This setup will take some time because of the size of the image.

## Login
When the container is running, execute this statement:
`docker exec -it jupyter bash -c 'jupyter notebook list'`{{execute}}

This will show something like:
```
Currently running servers:
http://0.0.0.0:8888/?token=12cf40356573270384da65aa5fb82a02b6b4c20679dc34d5 :: /home/jovyan
```

The token is the value behind `/?token=`. You need that for logging in.

Next, you can open the Jupyter Notebook at 
 https://[[HOST_SUBDOMAIN]]-8888-[[KATACODA_HOST]].environments.katacoda.com/

Note: you need the value of the Jupyter Token to login to the environment.