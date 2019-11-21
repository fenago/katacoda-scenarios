Now that you have launched your server instance, it is time to log in and start using it.

1. Click View Instances in your Amazon EC2 console if you have not done so already.
2. Copy the Public IP (down the bottom of the screen in Description) to your clipboard.
In this example my IP address is 54.186.97.77. Do not use this IP address, it will
not work as your server IP address will be different.
3. Open a Terminal and change directory to where you downloaded your key pair. Login
to your server using SSH, for example:
    ```
    ssh -i keras-aws-keypair.pem ec2-user@54.186.97.77
    ```
4. If prompted, type yes and press enter.
You are now logged into your server.
    ![](https://github.com/fenago/katacoda-scenarios/raw/master/deep-learning-computer-vision/deep-learning-computer-vision-aws/steps/7/1.JPG)


The instance will ask what Python environment you wish to use. I recommend using:
 **TensorFlow(+Keras2) with Python3 (CUDA 9.0 and Intel MKL-DNN)**

You can activate this virtual environment by typing:

```
source activate tensorflow_p36
```

You are now free to run your code.