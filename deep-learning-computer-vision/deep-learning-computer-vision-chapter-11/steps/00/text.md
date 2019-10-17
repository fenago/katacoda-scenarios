This tutorial is divided into four parts; they are:
1. Convolution in Convolutional Neural Networks
2. Convolution in Computer Vision
3. Power of Learned Filters
4. Worked Example of Convolutional Layers


#### Convolution in Convolutional Neural Networks
The convolutional neural network, or CNN for short, is a specialized type of neural network
model designed for working with two-dimensional image data, although they can be used with
one-dimensional and three-dimensional data. Central to the convolutional neural network is the
convolutional layer that gives the network its name. This layer performs an operation called a
convolution. In the context of a convolutional neural network, a convolution is a linear operation
that involves the multiplication of a set of weights with the input, much like a traditional neural
network. Given that the technique was designed for two-dimensional input, the multiplication
is performed between an array of input data and a two-dimensional array of weights, called a
filter or a kernel.


#### Convolution in Computer Vision
The idea of applying the convolutional operation to image data is not new or unique to
convolutional neural networks; it is a common technique used in computer vision. Historically,
filters were designed by hand by computer vision experts, which were then applied to an image
to result in a feature map or output from applying the filter that makes the analysis of the
image easier in some way. For example, below is a hand crafted 3 x 3 element filter for detecting
vertical lines:

```
0.0, 1.0, 0.0
0.0, 1.0, 0.0
0.0, 1.0, 0.0
```

Applying this filter to an image will result in a feature map that only contains vertical
lines. It is a vertical line detector. You can see this from the weight values in the filter; any
pixels values in the center vertical line will be positively activated and any on either side will be
negatively activated. Dragging this filter systematically across pixel values in an image can only
highlight vertical line pixels. A horizontal line detector could also be created and also applied
to the image, for example:

```
0.0, 0.0, 0.0
1.0, 1.0, 1.0
0.0, 0.0, 0.0
```
