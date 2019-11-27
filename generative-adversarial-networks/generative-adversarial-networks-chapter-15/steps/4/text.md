In this section, we will develop an LSGAN for the MNIST handwritten digit dataset. The first step is to define the models. Both the discriminator and the generator
will be based on the Deep Convolutional GAN, or DCGAN, architecture. This involves the use
of Convolution-BatchNorm-Activation layer blocks with the use of 2× 2 stride for downsampling
and transpose convolutional layers for upsampling. LeakyReLU activation layers are used in the
discriminator and ReLU activation layers are used in the generator. The discriminator expects
grayscale input images with the shape 28 × 28, the shape of images in the MNIST dataset, and
the output layer is a single node with a linear activation function. The model is optimized using
the mean squared error (MSE) loss function as per the LSGAN. The define discriminator()
function below defines the discriminator model.

```
# define the standalone discriminator model
def define_discriminator(in_shape=(28,28,1)):
# weight initialization
init = RandomNormal(stddev=0.02)
# define model
model = Sequential()
# downsample to 14x14
model.add(Conv2D(64, (4,4), strides=(2,2), padding='same', kernel_initializer=init,
input_shape=in_shape))
model.add(BatchNormalization())
model.add(LeakyReLU(alpha=0.2))
# downsample to 7x7
model.add(Conv2D(128, (4,4), strides=(2,2), padding='same', kernel_initializer=init))
model.add(BatchNormalization())
model.add(LeakyReLU(alpha=0.2))
# classifier
model.add(Flatten())
model.add(Dense(1, activation='linear', kernel_initializer=init))
# compile model with L2 loss
model.compile(loss='mse', optimizer=Adam(lr=0.0002, beta_1=0.5))
return model
```
