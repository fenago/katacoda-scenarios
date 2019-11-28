We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `generative-adversarial-networks/chapter_08/04_train_discriminator.py` to view file.

#### Run Code

Now, run the python code by running: `python 04_train_discriminator.py`{{execute}}


Running the example first defines the model, loads the CIFAR-10 dataset, then trains the
discriminator model.

**Note:** Your specific results may vary given the stochastic nature of the learning algorithm.
Consider running the example a few times and compare the average performance.
In this case, the discriminator model learns to tell the difference between real and randomly
generated CIFAR-10 images very quickly, in about 20 batches.

```
...
>16 real=100% fake=100%8.4. How to Define and Use the Generator Model 143
>17 real=100% fake=100%
>18 real=98% fake=100%
>19 real=100% fake=100%
>20 real=100% fake=100%
```

Now that we know how to define and train the discriminator model, we need to look at
developing the generator model.