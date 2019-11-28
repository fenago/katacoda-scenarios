
The generator model is more complex than the discriminator model. The generator is
an encoder-decoder model using a U-Net architecture. The model takes a source image (e.g.
satellite photo) and generates a target image (e.g. Google maps image). It does this by first
downsampling or encoding the input image down to a bottleneck layer, then upsampling or
decoding the bottleneck representation to the size of the output image. The U-Net architecture
means that skip-connections are added between the encoding layers and the corresponding
decoding layers, forming a U-shape. The encoder and decoder of the generator are comprised of
standardized blocks of convolutional, batch normalization, dropout, and activation layers. This
standardization means that we can develop helper functions to create each block of layers and
call it repeatedly to build-up the encoder and decoder parts of the model.
The define generator() function below implements the U-Net encoder-decoder generator
model. It uses the define encoder block() helper function to create blocks of layers for the
encoder and the decoder block() function to create blocks of layers for the decoder. The Tanh
activation function is used in the output layer, meaning that pixel values in the generated image
will be in the range [-1,1].

```
# define an encoder block
def define_encoder_block(layer_in, n_filters, batchnorm=True):
# weight initialization
init = RandomNormal(stddev=0.02)
# add downsampling layer
g = Conv2D(n_filters, (4,4), strides=(2,2), padding='same',
kernel_initializer=init)(layer_in)
# conditionally add batch normalization
if batchnorm:
g = BatchNormalization()(g, training=True)
# leaky relu activation
g = LeakyReLU(alpha=0.2)(g)
return g
# define a decoder block
def decoder_block(layer_in, skip_in, n_filters, dropout=True):
# weight initialization
init = RandomNormal(stddev=0.02)23.4. How to Develop and Train a Pix2Pix Model 491
# add upsampling layer
g = Conv2DTranspose(n_filters, (4,4), strides=(2,2), padding='same',
kernel_initializer=init)(layer_in)
# add batch normalization
g = BatchNormalization()(g, training=True)
# conditionally add dropout
if dropout:
g = Dropout(0.5)(g, training=True)
# merge with skip connection
g = Concatenate()([g, skip_in])
# relu activation
g = Activation('relu')(g)
return g
# define the standalone generator model
def define_generator(image_shape=(256,256,3)):
# weight initialization
init = RandomNormal(stddev=0.02)
# image input
in_image = Input(shape=image_shape)
# encoder model
e1 = define_encoder_block(in_image, 64, batchnorm=False)
e2 = define_encoder_block(e1, 128)
e3 = define_encoder_block(e2, 256)
e4 = define_encoder_block(e3, 512)
e5 = define_encoder_block(e4, 512)
e6 = define_encoder_block(e5, 512)
e7 = define_encoder_block(e6, 512)
# bottleneck, no batch norm and relu
b = Conv2D(512, (4,4), strides=(2,2), padding='same', kernel_initializer=init)(e7)
b = Activation('relu')(b)
# decoder model
d1 = decoder_block(b, e7, 512)
d2 = decoder_block(d1, e6, 512)
d3 = decoder_block(d2, e5, 512)
d4 = decoder_block(d3, e4, 512, dropout=False)
d5 = decoder_block(d4, e3, 256, dropout=False)
d6 = decoder_block(d5, e2, 128, dropout=False)
d7 = decoder_block(d6, e1, 64, dropout=False)
# output
g = Conv2DTranspose(3, (4,4), strides=(2,2), padding='same', kernel_initializer=init)(d7)
out_image = Activation('tanh')(g)
# define model
model = Model(in_image, out_image)
return model
```
