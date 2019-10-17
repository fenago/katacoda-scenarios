There are discrete architectural elements from milestone models that you can use in the design of
your own convolutional neural networks. Specifically, models that have achieved state-of-the-art
results for tasks like image classification use discrete architecture elements repeated multiple
times, such as the VGG block in the VGG models, the inception module in the GoogLeNet,
and the residual module in the ResNet. Once you are able to implement parameterized versions
of these architecture elements, you can use them in the design of your own models for computer
vision and other applications. In this tutorial, you will discover how to implement the key
architecture elements from milestone convolutional neural network models, from scratch.

After completing this tutorial, you will know:
- How to implement a VGG module used in the VGG-16 and VGG-19 convolutional neural
network models.
- How to implement the naive and optimized inception module used in the GoogLeNet
model.
- How to implement the identity residual module used in the ResNet model.
Let’s get started

#### Tutorial Overview
This tutorial is divided into three parts; they are:

1. How to implement VGG Blocks
2. How to implement the Inception Module
3. How to implement the Residual Module