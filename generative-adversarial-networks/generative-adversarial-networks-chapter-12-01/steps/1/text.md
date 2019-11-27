Generative Adversarial Networks, or GANs for short, is a deep learning neural network architecture for training a generator model for generating synthetic images. A problem with generative
models is that there is no objective way to evaluate the quality of the generated images. As
such, it is common to periodically generate and save images during the model training process
and use subjective human evaluation of the generated images in order to both evaluate the
quality of the generated images and to select a final generator model. Many attempts have been
made to establish an objective measure of generated image quality. An early and somewhat
widely adopted example of an objective evaluation method for generated images is the Inception
Score, or IS. In this tutorial, you will discover the inception score for evaluating the quality of
generated images. After completing this tutorial, you will know:
- How to calculate the inception score and the intuition behind what it measures.
- How to implement the inception score in Python with NumPy and the Keras deep learning
library.
- How to calculate the inception score for small images such as those in the CIFAR-10
dataset.

Let’s get started.
