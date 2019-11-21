
The generator is evaluated every 10 epochs, resulting in 10 evaluations, 10 plots of generated
images, and 10 saved models. In this case, we can see that the accuracy fluctuates over training.
When viewing the discriminator model’s accuracy score in concert with generated images, we
can see that the accuracy on fake examples does not correlate well with the subjective quality
of images, but the accuracy for real examples may. It is crude and possibly unreliable metric of
GAN performance, along with loss.

```
>Accuracy real: 51%, fake: 78%
>Accuracy real: 30%, fake: 95%
>Accuracy real: 75%, fake: 59%
>Accuracy real: 98%, fake: 11%
>Accuracy real: 27%, fake: 92%
>Accuracy real: 21%, fake: 92%
>Accuracy real: 29%, fake: 96%
>Accuracy real: 4%, fake: 99%7.7. Complete Example of GAN for MNIST 124
>Accuracy real: 18%, fake: 97%
>Accuracy real: 28%, fake: 89%
```
