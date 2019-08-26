To avoid being spammed with eleventy pages of output, we can use the --tail option:
`docker logs --tail 3 mycontainer`{{execute}}

**Note:** The parameter is the number of lines that we want to see.


#### Docker port mapping
In order to actually benefit from the container, we need to make it publicly accessible from the outside. This is where we will need to use the -p option with a few arguments while running the docker run command:


`docker run -d -p 8080:80 httpd`{{execute}}

```
3b1150b5034329cd9e70f90ee21531b8b1ab1d4a85141fd3a362cd40db80e193
```

Option -p maps container port 80 to your server port 8080. Verify that you have a httpd container exposed and a web server running:


`curl localhost:8080`{{execute}}

```
<html><body><h1>It works!</h1></body></html>
```
Inspecting the Docker container
While the container is running, we can inspect its parameters by using the docker inspect command. The output is provided in JSON format and it gives us a very comprehensive output:


`docker inspect backgroundcontainer`{{execute}}
[
   {
       "Id": "backgroundcontainerf26c24e02cd61d6a37bbc36106b3b0372073673c2983cb6f",
       ...
       output truncated for brevity
       ...
   }
]