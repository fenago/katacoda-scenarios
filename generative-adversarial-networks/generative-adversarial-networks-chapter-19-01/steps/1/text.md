Generative Adversarial Networks, or GANs, are an architecture for training generative models,
such as deep convolutional neural networks for generating images. The conditional generative
adversarial network, or cGAN for short, is a type of GAN that involves the conditional generation
of images by a generator model. Image generation can be conditional on a class label, if available,
allowing the targeted generated of images of a given type. The Auxiliary Classifier GAN, or
AC-GAN for short, is an extension of the conditional GAN that changes the discriminator to
predict the class label of a given image rather than receive it as input. It has the effect of
stabilizing the training process and allowing the generation of large high-quality images whilst
learning a representation in the latent space that is independent of the class label. In this
tutorial, you will discover how to develop an auxiliary classifier generative adversarial network
for generating photographs of clothing. After completing this tutorial, you will know:
- The auxiliary classifier GAN is a type of conditional GAN that requires that the discriminator predict the class label of a given image.
- How to develop generator, discriminator, and composite models for the AC-GAN.
- How to train, evaluate, and use an AC-GAN to generate photographs of clothing from the
Fashion-MNIST dataset.
Let’s get started.

19.1 Tutorial Overview
This tutorial is divided into five parts; they are:
1. Auxiliary Classifier Generative Adversarial Networks
2. Fashion-MNIST Clothing Photograph Dataset
3. How to Define AC-GAN Models

