Tutorial Overview
This tutorial is divided into five parts; they are:
1. Wasserstein Generative Adversarial Network
2. How to Implement Wasserstein Loss
3. Wasserstein GAN Implementation Details
4. How to Train a Wasserstein GAN Model
5. How to Generate Images With WGAN

#### What Is a Wasserstein GAN?
The Wasserstein GAN, or WGAN for short, was introduced by Martin Arjovsky, et al. in their
2017 paper titled Wasserstein GAN. It is an extension of the GAN that seeks an alternate way
of training the generator model to better approximate the distribution of data observed in a
given training dataset. Instead of using a discriminator to classify or predict the probability
of generated images as being real or fake, the WGAN changes or replaces the discriminator
model with a critic that scores the realness or fakeness of a given image. This change is
motivated by a mathematical argument that training the generator should seek a minimization
of the distance between the distribution of the data observed in the training dataset and the
distribution observed in generated examples. The argument contrasts different distribution
distance measures, such as Kullback-Leibler (KL) divergence, Jensen-Shannon (JS) divergence,
and the Earth-Mover (EM) distance, the latter also referred to as Wasserstein distance.

They demonstrate that a critic neural network can be trained to approximate the Wasserstein
distance, and, in turn, used to effectively train a generator model. Importantly, the Wasserstein
distance has the properties that it is continuous and differentiable and continues to provide a
linear gradient, even after the critic is well trained.