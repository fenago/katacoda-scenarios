
Docker import is used to Import the contents from a tarball to create a filesystem image. Let’s import from a tar file.

```
Usage
docker import [OPTIONS] file|URL|- [REPOSITORY[:TAG]]
```

This time, we import the container hlf_export.tar.
`cat hlf_export.tar  | docker import - hlf-custom`{{execute}}

**Note:** Please wait for the above command to complete, It will take around 1 minutes to complete.

#### Validate
You can verify import was successful by running `docker images`{{execute}} command.