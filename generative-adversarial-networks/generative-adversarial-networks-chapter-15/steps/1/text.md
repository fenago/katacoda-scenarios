The Least Squares Generative Adversarial Network, or LSGAN for short, is an extension to the
GAN architecture that addresses the problem of vanishing gradients and loss saturation. It is
motivated by the desire to provide a signal to the generator about fake samples that are far from
the discriminator model’s decision boundary for classifying them as real or fake. The further
the generated images are from the decision boundary, the larger the error signal provided to the
generator, encouraging the generation of more realistic images. The LSGAN can be implemented
with a minor change to the output layer of the discriminator layer and the adoption of the least
squares, or L2, loss function. In this tutorial, you will discover how to develop a least squares
generative adversarial network.

After completing this tutorial, you will know:
- The LSGAN addresses vanishing gradients and loss saturation of the deep convolutional
GAN.
- The LSGAN can be implemented by a mean squared error or L2 loss function for the
discriminator model.
- How to implement the LSGAN model for generating handwritten digits for the MNIST
dataset.
Let’s get started