
The generator is evaluated every 10 epochs, resulting in 20 evaluations, 20 plots of generated
images, and 20 saved models. In this case, we can see that the accuracy fluctuates over training.
When viewing the discriminator model’s accuracy score in concert with generated images, we
can see that the accuracy on fake examples does not correlate well with the subjective quality
of images, but the accuracy for real examples may. It is a crude and possibly unreliable metric
of GAN performance, along with loss.

```
>Accuracy real: 55%, fake: 89%
>Accuracy real: 50%, fake: 75%
>Accuracy real: 49%, fake: 86%
>Accuracy real: 60%, fake: 79%
>Accuracy real: 49%, fake: 87%
...
```
