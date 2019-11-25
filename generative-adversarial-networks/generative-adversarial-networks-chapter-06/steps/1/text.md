Generative Adversarial Networks, or GANs for short, are a deep learning architecture for training
powerful generator models. A generator model is capable of generating new artificial samples
that plausibly could have come from an existing distribution of samples. GANs are comprised
of both generator and discriminator models. The generator is responsible for generating new
samples from the domain, and the discriminator is responsible for classifying whether samples
are real or fake (generated). Importantly, the performance of the discriminator model is used to
update both the model weights of the discriminator itself and the generator model. This means
that the generator never actually sees examples from the domain and is adapted based on how
well the discriminator performs.

This is a complex type of model both to understand and to train. One approach to better
understand the nature of GAN models and how they can be trained is to develop a model from
scratch for a very simple task. A simple task that provides a good context for developing a
simple GAN from scratch is a one-dimensional function. This is because both real and generated
samples can be plotted and visually inspected to get an idea of what has been learned. A
simple function also does not require sophisticated neural network models, meaning the specific
generator and discriminator models used on the architecture can be easily understood. In this
tutorial, we will select a simple one-dimensional function and use it as the basis for developing
and evaluating a generative adversarial network from scratch using the Keras deep learning
library. After completing this tutorial, you will know:
- The benefit of developing a generative adversarial network from scratch for a simple
one-dimensional function.
- How to develop separate discriminator and generator models, as well as a composite model
for training the generator via the discriminator’s predictive behavior.
- How to subjectively evaluate generated samples in the context of real examples from the
problem domain.
Let’s get started.