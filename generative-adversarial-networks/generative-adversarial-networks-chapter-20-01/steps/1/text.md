How to Develop a Semi-Supervised
GAN (SGAN)
Semi-supervised learning is the challenging problem of training a classifier in a dataset that
contains a small number of labeled examples and a much larger number of unlabeled examples.
The Generative Adversarial Network, or GAN, is an architecture that makes effective use of
large, unlabeled datasets to train an image generator model via an image discriminator model.
The discriminator model can be used as a starting point for developing a classifier model in
some cases.
The semi-supervised GAN, or SGAN, model is an extension of the GAN architecture that
involves the simultaneous training of a supervised discriminator, unsupervised discriminator,
and a generator model. The result is both a supervised classification model that generalizes
well to unseen examples and a generator model that outputs plausible examples of images from
the domain. In this tutorial, you will discover how to develop a Semi-Supervised Generative
Adversarial Network from scratch. 