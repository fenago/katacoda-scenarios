GANs are difficult to train. The reason they are difficult to train is that both the generator
model and the discriminator model are trained simultaneously in a zero sum game. This means
that improvements to one model come at the expense of the other model. The goal of training
two models involves finding a point of equilibrium between the two competing concerns. It
also means that every time the parameters of one of the models are updated, the nature of
the optimization problem that is being solved is changed. This has the effect of creating a
dynamic system. In neural network terms, the technical challenge of training two competing
neural networks at the same time is that they can fail to converge.

It is important to develop an intuition for both the normal convergence of a GAN model and
unusual convergence of GAN models, sometimes called failure modes. In this tutorial, we will
first develop a stable GAN model for a simple image generation task in order to establish what
normal convergence looks like and what to expect more generally. We will then impair the GAN
models in different ways and explore a range of failure modes that you may encounter when
training GAN models. These scenarios will help you to develop an intuition for what to look for
or expect when a GAN model is failing to train, and ideas for what you could do about it.