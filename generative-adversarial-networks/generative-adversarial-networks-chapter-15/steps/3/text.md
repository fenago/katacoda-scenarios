This tutorial is divided into three parts; they are:
- What Is Least Squares GAN
- How to Develop an LSGAN for MNIST
- How to Generate Images With LSGAN

#### What Is Least Squares GAN
The standard Generative Adversarial Network, or GAN for short, is an effective architecture for
training an unsupervised generative model. The architecture involves training a discriminator
model to tell the difference between real (from the dataset) and fake (generated) images, and
using the discriminator, in turn, to train the generator model. The generator is updated in such
a way that it is encouraged to generate images that are more likely to fool the discriminator.
The discriminator is a binary classifier and is trained using binary cross-entropy loss function.
A limitation of this loss function is that it is primarily concerned with whether the predictions
are correct or not, and less so with how correct or incorrect they might be.

This can be conceptualized in two dimensions as a line or decision boundary separating dots
that represent real and fake images. The discriminator is responsible for devising the decision
boundary to best separate real and fake images and the generator is responsible for creating new
points that look like real points, confusing the discriminator. The choice of cross-entropy loss
means that points generated far from the boundary are right or wrong, but provide very little
gradient information to the generator on how to generate better images. This small gradient for
generated images far from the decision boundary is referred to as a vanishing gradient problem
or a loss saturation. The loss function is unable to give a strong signal as to how to best update
the model.