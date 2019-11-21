Consider running the example a few times and compare the average performance.
In this case, the discriminator and generator loss both sit around values of about 0.6 to 0.7
over the course of training

```
>100, 464/468, d1=0.681, d2=0.685 g=0.693
>100, 465/468, d1=0.691, d2=0.700 g=0.703
>100, 466/468, d1=0.691, d2=0.703 g=0.706
>100, 467/468, d1=0.698, d2=0.699 g=0.699
>100, 468/468, d1=0.699, d2=0.695 g=0.708
```

At the end of training, the generator model will be saved to file with the filename generator.h5.

This model can be loaded and used to generate new random but plausible samples from the
Fashion-MNIST dataset. The example below loads the saved model and generates 100 random
items of clothing.
