
Line plots for loss and accuracy are created and saved at the end of the run. The figure
contains two subplots. The top subplot shows line plots for the discriminator loss for real images
(blue), discriminator loss for generated fake images (orange), and the generator loss for generated
fake images (green). We can see that all three losses are somewhat erratic early in the run
before stabilizing around epoch 100 to epoch 300. Losses remain stable after that, although the
variance increases. This is an example of the normal or expected loss during training. Namely,
discriminator loss for real and fake samples is about the same at or around 0.5, and loss for the
generator is slightly higher between 0.5 and 2.0. If the generator model is capable of generating
plausible images, then the expectation is that those images would have been generated between
epochs 100 and 300 and likely between 300 and 450 as well.

The bottom subplot shows a line plot of the discriminator accuracy on real (blue) and fake
(orange) images during training. We see a similar structure as the subplot of loss, namely that
accuracy starts off quite different between the two image types, then stabilizes between epochs
100 to 300 at around 70% to 80%, and remains stable beyond that, although with increased
variance. The time scales (e.g. number of iterations or training epochs) for these patterns and
absolute values will vary across problems and types of GAN models, although the plot provides
a good baseline for what to expect when training a stable GAN model.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-10/steps/1.PNG)

Finally, we can review samples of generated images. We are generating images using a
reverse grayscale color map, meaning that the normal white figure on a background is inverted
to a black figure on a white background. This was done to make the generated figures easier to
review. As we might expect, samples of images generated before epoch 100 are relatively poor
in quality.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-10/steps/2.PNG)

Samples of images generated between epochs 100 and 300 are plausible, and perhaps the
best quality.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-10/steps/3.PNG)

And samples of generated images after epoch 300 remain plausible, although perhaps have
more noise, e.g. background noise.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-10/steps/4.PNG)

