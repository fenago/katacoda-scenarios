This tutorial is divided into five parts; they are:
1. Convolutional Layer
2. Problem of Border Effects
3. Effect of Filter Size (Kernel Size)
4. Fix the Border Effect Problem With Padding
5. Downsample Input With Stride



#### Convolutional Layer
In a convolutional neural network, a convolutional layer is responsible for the systematic
application of one or more filters to an input. The multiplication of the filter to the input
image results in a single output. The input is typically three-dimensional images (e.g. rows,
columns and channels), and in turn, the filters are also three-dimensional with the same number
of channels and fewer rows and columns than the input image. As such, the filter is repeatedly
applied to each part of the input image, resulting in a two-dimensional output map of activations,
called a feature map. Keras provides an implementation of the convolutional layer called a
Conv2D layer.
It requires that you specify the expected shape of the input images in terms of rows (height),
columns (width), and channels (depth) or [rows, columns, channels]. The filter contains
the weights that must be learned during the training of the layer. The filter weights represent
the structure or feature that the filter will detect and the strength of the activation indicates
the degree to which the feature was detected. The layer requires that both the number of filters
be specified and that the shape of the filters be specified.