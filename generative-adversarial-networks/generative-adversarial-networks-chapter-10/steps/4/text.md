In this section, we will train a stable GAN to generate images of a handwritten digit. Specifically,
we will use the digit ‘8’ from the MNIST handwritten digit dataset. The results of this model
will establish both a stable GAN that can be used for later experimentation and a profile for
what generated images and learning curves look like for a stable GAN training process.

The first step is to define the models. The discriminator model takes as input one 28 × 28
grayscale image and outputs a binary prediction as to whether the image is real (class = 1) or
fake (class = 0). It is implemented as a modest convolutional neural network using best practices
for GAN design such as using the LeakyReLU activation function with a slope of 0.2, batch
normalization, using a 2 × 2 stride to downsample, and the adam version of stochastic gradient
descent with a learning rate of 0.0002 and a momentum of 0.5 The define discriminator()
function below implements this, defining and compiling the discriminator model and returning
it. The input shape of the image is parameterized as a default function argument to make it
clear.

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
model.add(Conv2D(64, (4,4), strides=(2,2), padding='same', kernel_initializer=init))
model.add(BatchNormalization())
model.add(LeakyReLU(alpha=0.2))
# classifier
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))
# compile model
opt = Adam(lr=0.0002, beta_1=0.5)
model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])
return model
```
