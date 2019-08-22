
Docker export is used to export the container’s file system into a tar file. Let’s export the container we setup into a tar file.
`docker export hlf > hlf_export.tar`{{execute}}

```
Usage
docker export [OPTIONS] CONTAINER
```

#### Validate
You can verify export was successful by listing contents of the directory  on your system by running `ls`{{execute}} command.




