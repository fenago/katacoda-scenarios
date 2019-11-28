We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `generative-adversarial-networks/chapter_10/01_normal_train_gain.py` to view file.

#### Run Code

Now, run the python code by running: `python 01_normal_train_gain.py`{{execute}}


Running the example is quick, taking approximately 10 minutes on modern hardware without
a GPU.

**Note:** Your specific results may vary given the stochastic nature of the learning algorithm.
Consider running the example a few times and compare the average performance.

First, the loss and accuracy of the discriminator and loss for the generator model are reported
to the console each iteration of the training loop. This is important. A stable GAN will have
a discriminator loss around 0.5, typically between 0.5 and maybe as high as 0.7 or 0.8. The
generator loss is typically higher and may hover around 1.0, 1.5, 2.0, or even higher.
The accuracy of the discriminator on both real and generated (fake) images will not be
50%, but should typically hover around 70% to 80%. For both the discriminator and generator,
behaviors are likely to start off erratic and move around a lot before the model converges to a
stable equilibrium.

```
>1, d1=0.859, d2=0.664 g=0.872, a1=37, a2=59
>2, d1=0.190, d2=1.429 g=0.555, a1=100, a2=10
>3, d1=0.094, d2=1.467 g=0.597, a1=100, a2=4
>4, d1=0.097, d2=1.315 g=0.686, a1=100, a2=9
>5, d1=0.100, d2=1.241 g=0.714, a1=100, a2=9
...
>446, d1=0.593, d2=0.546 g=1.330, a1=76, a2=82
>447, d1=0.551, d2=0.739 g=0.981, a1=82, a2=39
>448, d1=0.628, d2=0.505 g=1.420, a1=79, a2=89
>449, d1=0.641, d2=0.533 g=1.381, a1=60, a2=85
>450, d1=0.550, d2=0.731 g=1.100, a1=76, a2=42
```
