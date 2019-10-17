Convolutional layers in a convolutional neural network systematically apply learned filters to
input images in order to create feature maps that summarize the presence of those features
in the input. Convolutional layers prove very effective, and stacking convolutional layers in
deep models allows layers close to the input to learn low-level features (e.g. lines) and layers
deeper in the model to learn high-order or more abstract features, like shapes or specific objects.
A limitation of the feature map output of convolutional layers is that they record the precise
position of features in the input. This means that small movements in the position of the feature
in the input image will result in a different feature map. This can happen with re-cropping,
rotation, shifting, and other minor changes to the input image.

A common approach to addressing this problem from signal processing is called down
sampling. This is where a lower resolution version of an input signal is created that still contains
the large or important structural elements, without the fine detail that may not be as useful to
the task. Down sampling can be achieved with convolutional layers by changing the stride of
the convolution across the image. A more robust and common approach is to use a pooling
layer. A pooling layer is a new layer added after the convolutional layer. Specifically, after a
nonlinearity (e.g. ReLU) has been applied to the feature maps output by a convolutional layer;
for example the layers in a model may look as follows:

1. Input Image.
2. Convolutional Layer.
3. Nonlinearity.
4. Pooling Layer.

The addition of a pooling layer after the convolutional layer is a common pattern used for
ordering layers within a convolutional neural network that may be repeated one or more times
in a given model. The pooling layer operates upon each feature map separately to create a new
set of the same number of pooled feature maps. Pooling involves selecting a pooling operation,
much like a filter to be applied to feature maps. The size of the pooling operation or filter is
smaller than the size of the feature map; specifically, it is almost always 2 x 2 pixels applied
with a stride of 2 pixels.


This means that the pooling layer will always reduce the size of each feature map by a factor
of 2, e.g. each dimension is halved, reducing the number of pixels or values in each feature map
to one quarter the size. For example, a pooling layer applied to a feature map of 6 x 6 (36
pixels) will result in an output pooled feature map of 3 x 3 (9 pixels). The pooling operation is
specified, rather than learned. Two common functions used in the pooling operation are:

- Average Pooling: Calculate the average value for each patch on the feature map.
- Maximum Pooling (or Max Pooling): Calculate the maximum value for each patch of
the feature map.

The result of using a pooling layer and creating downsampled or pooled feature maps is a
summarized version of the features detected in the input. They are useful as small changes
in the location of the feature in the input detected by the convolutional layer will result in a
pooled feature map with the feature in the same location. This capability added by pooling is
called the model’s invariance to local translation.