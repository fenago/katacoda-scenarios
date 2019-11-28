We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `generative-adversarial-networks/chapter_07/04_train_discriminator.py` to view file.

#### Run Code

Now, run the python code by running: `python 04_train_discriminator.py`{{execute}}

Running the example first defines the model, loads the MNIST dataset, then trains the
discriminator model.

**Note:** Your specific results may vary given the stochastic nature of the learning algorithm.
Consider running the example a few times and compare the average performance.
In this case, the discriminator model learns to tell the difference between real and generated
MNIST images very quickly, in about 50 batches.

```
...
>96 real=100% fake=100%
>97 real=100% fake=100%
>98 real=100% fake=100%
>99 real=100% fake=100%
>100 real=100% fake=100%
```
