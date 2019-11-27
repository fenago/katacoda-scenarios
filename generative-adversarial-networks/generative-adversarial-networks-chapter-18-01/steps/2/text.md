The Generative Adversarial Network, or GAN for short, is an architecture for training a
generative model, such as a model for generating synthetic images. It involves the simultaneous
training of the generator model for generating images with a discriminator model that learns to
classify images as either real (from the training dataset) or fake (generated). The two models
compete in a zero-sum game such that convergence of the training process involves finding a
balance between the generator’s skill in generating convincing images and the discriminator’s in
being able to detect them. The generator model takes as input a random point from a latent
space, typically 50 to 100 random Gaussian variables. The generator applies a unique meaning
to the points in the latent space via training and maps points to specific output synthetic images.
This means that although the latent space is structured by the generator model, there is no
control over the generated image.

The latent space can be explored and generated images compared in an attempt to understand
the mapping that the generator model has learned. Alternatively, the generation process can
be conditioned, such as via a class label, so that images of a specific type can be created on
demand. This is the basis for the Conditional Generative Adversarial Network, CGAN or cGAN
for short. Another approach is to provide control variables as input to the generator, along
with the point in latent space (noise). The generator can be trained to use the control variables
to influence specific properties of the generated images. This is the approach taken with the
Information Maximizing Generative Adversarial Network, or InfoGAN for short.