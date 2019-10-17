This section offers some tips for running your code on AWS.

#### Copy Scripts and Data to AWS
You can get started quickly by copying your files to your running AWS instance. For example,
you can copy the examples provided with this book to your AWS instance using the scp
command as follows:

```
scp -i keras-aws-keypair.pem -r src ec2-user@54.186.97.77:~/
```


This will copy the entire src/ directory to your home directory on your AWS instance. You
can easily adapt this example to get your larger datasets from your workstation onto your AWS
instance. Note that Amazon may impose charges for moving very large amounts of data in and
out of your AWS instance. Refer to Amazon documentation for relevant charges.


#### Run Models on AWS
You can run your scripts on your AWS instance as per normal:
```
python filename.py
```

You are using AWS to create large neural network models that may take hours or days to
train. As such, it is a better idea to run your scripts as a background job. This allows you to
close your terminal and your workstation while your AWS instance continues to run your script.
You can easily run your script as a background process as follows:

```
nohup /path/to/script >/path/to/script.log 2>&1 < /dev/null &
```

You can then check the status and results in your script.log file later