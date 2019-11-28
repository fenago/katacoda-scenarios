
We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `generative-adversarial-networks/chapter_10/02_mode_collapse.py` to view file.

#### Run Code
Now, run the python code by running: `python 02_mode_collapse.py`{{execute}}

Running the example will report the loss and accuracy each step of training, as before.
In this case, the loss for the discriminator sits in a sensible range, although the loss for the
generator jumps up and down. The accuracy for the discriminator also shows higher values,
many around 100%, meaning that for many batches, it has perfect skill at identifying real or
fake examples, a bad sign for image quality or diversity.

```
>1, d1=0.963, d2=0.699 g=0.614, a1=28, a2=54
>2, d1=0.185, d2=5.084 g=0.097, a1=96, a2=0
>3, d1=0.088, d2=4.861 g=0.065, a1=100, a2=0
>4, d1=0.077, d2=4.202 g=0.090, a1=100, a2=0
>5, d1=0.062, d2=3.533 g=0.128, a1=100, a2=0
...
>446, d1=0.277, d2=0.261 g=0.684, a1=95, a2=100
>447, d1=0.201, d2=0.247 g=0.713, a1=96, a2=100
>448, d1=0.285, d2=0.285 g=0.728, a1=89, a2=100
>449, d1=0.351, d2=0.467 g=1.184, a1=92, a2=81
>450, d1=0.492, d2=0.388 g=1.351, a1=76, a2=100
```

The figure with learning curve and accuracy line plots is created and saved. In the top
subplot, we can see the loss for the generator (green) oscillating from sensible to high values
over time, with a period of about 25 model updates (batches). We can also see some small
oscillations in the loss for the discriminator on real and fake samples (orange and blue). In the
bottom subplot, we can see that the discriminator’s classification accuracy for identifying fake
images remains high throughout the run. This suggests that the generator is poor at generating
examples in some consistent way that makes it easy for the discriminator to identify the fake
images.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-10/steps/5.PNG)

Reviewing generated images shows the expected feature of mode collapse, namely many
nearly identical generated examples, regardless of the input point in the latent space. It just so
happens that we have changed the dimensionality of the latent space to be dramatically small
to force this effect. I have chosen an example of generated images that helps to make this clear.
There appear to be only a few types of figure-eights in the image, one leaning left, one leaning
right, and one sitting up with a blur. I have drawn boxes around some of the similar examples
in the image below to make this clearer.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-10/steps/6.PNG)

A mode collapse is less common during training given the findings from the DCGAN model
architecture and training configuration. In summary, you can identify a mode collapse as follows:
- The loss for the generator, and probably the discriminator, is expected to oscillate over
time.
- The generator model is expected to generate identical output images from different points
in the latent space.

