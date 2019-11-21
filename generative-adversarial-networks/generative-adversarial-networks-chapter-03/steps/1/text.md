Generative Adversarial Networks, or GANs, are an architecture for training generative models,
such as deep convolutional neural networks for generating images. The GAN architecture is
comprised of both a generator and a discriminator model. The generator is responsible for
creating new outputs, such as images, that plausibly could have come from the original dataset.
The generator model is typically implemented using a deep convolutional neural network and
results-specialized layers that learn to fill in features in an image rather than extract features
from an input image.
Two common types of layers that can be used in the generator model are a upsample
layer that simply doubles the dimensions of the input and the transpose convolutional layer
that performs an inverse convolution operation. In this tutorial, you will discover how to use
Upsampling and Transpose Convolutional Layers in Generative Adversarial Networks when
generating images. After completing this tutorial, you will know:
- Generative models in the GAN architecture are required to upsample input data in order
to generate an output image.
- The Upsampling layer is a simple layer with no weights that will double the dimensions of
input and can be used in a generative model when followed by a traditional convolutional
layer.
- The Transpose Convolutional layer is an inverse convolutional layer that will both upsample
input and learn how to fill in details during the model training process.
Let’s get started.