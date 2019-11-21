Generative Adversarial Networks, or GANs, are an architecture for training generative models,
such as deep convolutional neural networks for generating images. Although GAN models are
capable of generating new random plausible examples for a given dataset, there is no way to
control the types of images that are generated other than trying to figure out the complex
relationship between the latent space input to the generator and the generated images. The
conditional generative adversarial network, or cGAN for short, is a type of GAN that involves
the conditional generation of images by a generator model. Image generation can be conditional
on a class label, if available, allowing the targeted generated of images of a given type. In this
tutorial, you will discover how to develop a conditional generative adversarial network for the
targeted generation of items of clothing.

Let’s get started.

#### Tutorial Overview
This tutorial is divided into five parts; they are:
1. Conditional Generative Adversarial Network
2. Fashion-MNIST Clothing Photograph Dataset