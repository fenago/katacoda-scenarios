This tutorial is divided into five parts; they are:
1. Convolutions Over Channels
2. Problem of Too Many Feature Maps
3. Downsample Feature Maps With 1 x 1 Filters
4. Examples of How to Use 1 x 1 Convolutions
5. Examples of 1 x 1 Filters in CNN Model Architectures

#### Convolutions Over Channels
Recall that a convolutional operation is a linear application of a smaller filter to a larger input
that results in an output feature map. A filter applied to an input image or input feature map
always results in a single number. The systematic left-to-right and top-to-bottom application
of the filter to the input results in a two-dimensional feature map. One filter creates one
corresponding feature map. A filter must have the same depth or number of channels as the
input, yet, regardless of the depth of the input and the filter, the resulting output is a single
number and one filter creates a feature map with a single channel. Let’s make this concrete
with some examples:

- If the input has one channel such as a grayscale image, then a 3 x 3 filter will be applied
in 3 x 3 x 1 blocks.
- If the input image has three channels for red, green, and blue, then a 3 x 3 filter will be
applied in 3 x 3 x 3 blocks.
- If the input is a block of feature maps from another convolutional or pooling layer and
has the depth of 64, then the 3 x 3 filter will be applied in 3 x 3 x 64 blocks to create the
single values to make up the single output feature map.

The depth of the output of one convolutional layer is only defined by the number of parallel
filters applied to the input