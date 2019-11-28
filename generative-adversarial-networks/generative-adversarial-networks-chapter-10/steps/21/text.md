We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `generative-adversarial-networks/chapter_10/04_different_convergence_failure.py` to view file.

#### Run Code

Now, run the python code by running: `python 04_different_convergence_failure.py`{{execute}}

Running the example reports the loss and accuracy for each step during training, as before.
As we expected, the loss for the discriminator rapidly falls to a value close to zero, where it
remains, and classification accuracy for the discriminator on real and fake examples remains at
100%.

```
>1, d1=0.728, d2=0.902 g=0.763, a1=54, a2=12
>2, d1=0.001, d2=4.509 g=0.033, a1=100, a2=0
>3, d1=0.000, d2=0.486 g=0.542, a1=100, a2=76
>4, d1=0.000, d2=0.446 g=0.733, a1=100, a2=82
>5, d1=0.002, d2=0.855 g=0.649, a1=100, a2=46
...
>446, d1=0.000, d2=0.000 g=10.410, a1=100, a2=100
>447, d1=0.000, d2=0.000 g=10.414, a1=100, a2=100
>448, d1=0.000, d2=0.000 g=10.419, a1=100, a2=100
>449, d1=0.000, d2=0.000 g=10.424, a1=100, a2=100
>450, d1=0.000, d2=0.000 g=10.427, a1=100, a2=100
```

A plot of the learning curves and accuracy from training the model with this single change
is created. The plot shows that this change causes the loss for the discriminator to crash down
to a value close to zero and remain there. An important difference for this case is that the loss
for the generator rises quickly and continues to rise for the duration of training.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-10/steps/9.PNG)

We can review the properties of a convergence failure as follows:
- The loss for the discriminator is expected to rapidly decrease to a value close to zero where
it remains during training.
- The loss for the generator is expected to either decrease to zero or continually decrease
during training.
- The generator is expected to produce extremely low-quality images that are easily identified
as fake by the discriminator.