
The generator model is more complex than the discriminator model. The generator is an
encoder-decoder model architecture. The model takes a source image (e.g. horse photo) and
generates a target image (e.g. zebra photo). It does this by first downsampling or encoding
the input image down to a bottleneck layer, then interpreting the encoding with a number of
ResNet layers that use skip connections, followed by a series of layers that upsample or decode
the representation to the size of the output image. First, we need a function to define the
ResNet blocks. These are blocks comprised of two 3 × 3 CNN layers where the input to the
block is concatenated to the output of the block, channel-wise.
This is implemented in the resnet block() function that creates two Convolution-InstanceNorm
blocks with 3 × 3 filters and 1 × 1 stride and without a ReLU activation after the second block,
matching the official Torch implementation in the build conv block() function. Same padding
is used instead of reflection padded recommended in the paper for simplicity.

```
# generator a resnet block
def resnet_block(n_filters, input_layer):
# weight initialization
init = RandomNormal(stddev=0.02)
# first layer convolutional layer
g = Conv2D(n_filters, (3,3), padding='same', kernel_initializer=init)(input_layer)
g = InstanceNormalization(axis=-1)(g)
g = Activation('relu')(g)
# second convolutional layer
g = Conv2D(n_filters, (3,3), padding='same', kernel_initializer=init)(g)
g = InstanceNormalization(axis=-1)(g)
# concatenate merge channel-wise with input layer
g = Concatenate()([g, input_layer])
return g
```
