
We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `generative-adversarial-networks/chapter_10/03_convergence_failure.py` to view file.

#### Run Code
Now, run the python code by running: `python 03_convergence_failure.py`{{execute}}

Running the example reports loss and accuracy for each model update. A clear sign of this
type of failure is the rapid drop of the discriminator loss towards zero, where it remains. This is what we see in this case.

```
>1, d=0.514, g=0.969, a=80
>2, d=0.475, g=0.395, a=74
>3, d=0.452, g=0.223, a=69
>4, d=0.302, g=0.220, a=85
>5, d=0.177, g=0.195, a=100
>6, d=0.122, g=0.200, a=100
>7, d=0.088, g=0.179, a=100
>8, d=0.075, g=0.159, a=100
>9, d=0.071, g=0.167, a=100
>10, d=0.102, g=0.127, a=100
...
>446, d=0.000, g=0.001, a=100
>447, d=0.000, g=0.001, a=100
>448, d=0.000, g=0.001, a=100
>449, d=0.000, g=0.001, a=100
>450, d=0.000, g=0.001, a=100
```

Line plots of learning curves and classification accuracy are created. The top subplot shows
the loss for the discriminator (blue) and generator (orange) and clearly shows the drop of both
values down towards zero over the first 20 to 30 iterations, where it remains for the rest of the
run. The bottom subplot shows the discriminator classification accuracy sitting on 100% for the
same period, meaning the model is perfect at identifying real and fake images. The expectation
is that there is something about fake images that makes them very easy for the discriminator to
identify.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-10/steps/7.PNG)

Finally, reviewing samples of generated images makes it clear why the discriminator is so
successful. Samples of images generated at each epoch are all very low quality, showing static,
perhaps with a faint figure eight in the background.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-10/steps/8.PNG)
