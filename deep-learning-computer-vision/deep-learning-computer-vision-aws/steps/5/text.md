
- Enter Deep Learning AMI in the Search community AMIs search box and press enter.C.3. Launch Your Server Instance 533
    ![](https://github.com/fenago/katacoda-scenarios/raw/master/deep-learning-computer-vision/deep-learning-computer-vision-aws/steps/5/1.JPG)

- Click Select to choose the AMI in the search result.

- Now you need to select the hardware on which to run the image. Scroll down and select
the p3.2xlarge hardware (I used to recommend g2 or g3 instances and p2 instances, but
the p3 instances2 are newer and faster). This includes a Tesla V100 GPU that we can use
to significantly increase the training speed of our models. It also includes 8 CPU Cores,
61GB of RAM and 16GB of GPU RAM. Note: using this instance will cost approximately 3 USD/hour.
    ![](https://github.com/fenago/katacoda-scenarios/raw/master/deep-learning-computer-vision/deep-learning-computer-vision-aws/steps/5/2.JPG)

- Click Review and Launch to finalize the configuration of your server instance.

-  Click the Launch button.

- Select Your Key Pair.
If you have a key pair because you have used EC2 before, select Choose an existing key pair
and choose your key pair from the list. Then check I acknowledge.... If you do not have a key
pair, select the option Create a new key pair and enter a Key pair name such as keras-keypair.
Click the Download Key Pair button.
    ![](https://github.com/fenago/katacoda-scenarios/raw/master/deep-learning-computer-vision/deep-learning-computer-vision-aws/steps/5/3.JPG)

