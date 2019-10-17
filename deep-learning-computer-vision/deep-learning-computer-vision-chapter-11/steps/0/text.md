Convolution and the convolutional layer are the major building blocks used in convolutional
neural networks. A convolution is the simple application of a filter to an input that results in an
activation. Repeated application of the same filter to an input results in a map of activations
called a feature map, indicating the locations and strength of a detected feature in an input,
such as an image. The innovation of convolutional neural networks is the ability to automatically
learn a large number of filters in parallel specific to a training dataset under the constraints of
a specific predictive modeling problem, such as image classification. The result is that highly
specific features can be detected anywhere on input images. In this tutorial, you will discover
how convolutions work in the convolutional neural network. After completing this tutorial, you
will know:
- Convolutional neural networks apply a filter to an input to create a feature map that
summarizes the presence of detected features in the input.
- Filters can be handcrafted, such as line detectors, but the innovation of convolutional
neural networks is to learn the filters during training in the context of a specific prediction
problem.
- How to calculate the feature map for one- and two-dimensional convolutional layers in a
convolutional neural network.
Let’s get started.
