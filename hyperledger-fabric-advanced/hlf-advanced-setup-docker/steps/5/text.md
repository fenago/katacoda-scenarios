
Docker export is used to export the container’s file system into a tar file. Let’s export the container we setup into a tar file.
`docker export hlf > hlf_export.tar`{{execute}}

**Note:** Please wait for the above command to complete, It will take around 1 minutes to complete.

```
Usage
docker export [OPTIONS] CONTAINER
```

#### Validate
You can verify export was successful by listing contents of the directory  on your system by running `ls`{{execute}} command.


