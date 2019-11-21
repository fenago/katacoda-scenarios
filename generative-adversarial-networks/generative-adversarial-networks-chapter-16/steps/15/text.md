Line plots for loss are created and saved at the end of the run. The plot shows the loss for
the critic on real samples (blue), the loss for the critic on fake samples (orange), and the loss for
the critic when updating the generator with fake samples (green). There is one important factor
when reviewing learning curves for the WGAN and that is the trend. The benefit of the WGAN
is that the loss correlates with generated image quality. Lower loss means better quality images,
for a stable training process. In this case, lower loss specifically refers to lower Wasserstein loss
for generated images as reported by the critic (orange line). This sign of this loss is not inverted
by the target label (e.g. the target label is 1.0), therefore, a well-performing WGAN should
show this line trending down as the image quality of the generated model is increased.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-16/steps/11/1.PNG)

In this case, more training seems to result in better quality generated images, with a major
hurdle occurring around epoch 200-300 after which quality remains pretty good for the model.
Before and around this hurdle, image quality is poor; for example:

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-16/steps/11/2.PNG)

After this epoch, the WGAN begins to generate plausible handwritten digits

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-16/steps/11/3.PNG)
