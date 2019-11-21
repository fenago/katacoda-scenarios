In this section, we will develop an unconditional GAN for the Fashion-MNIST dataset. The
first step is to define the models. The discriminator model takes as input one 28 × 28 grayscale
image and outputs a binary prediction as to whether the image is real (class = 1) or fake
(class = 0). It is implemented as a modest convolutional neural network using best practices for
GAN design such as using the LeakyReLU activation function with a slope of 0.2, using a 2 × 2
stride to downsample, and the adam version of stochastic gradient descent with a learning rate
of 0.0002 and a momentum of 0.5 The define discriminator() function below implements
this, defining and compiling the discriminator model and returning it. The input shape of the
image is parameterized as a default function argument in case you want to re-use the function
for your own image data later.

```
# define the standalone discriminator model
def define_discriminator(in_shape=(28,28,1)):
model = Sequential()
# downsample
model.add(Conv2D(128, (3,3), strides=(2,2), padding='same', input_shape=in_shape))
model.add(LeakyReLU(alpha=0.2))
# downsample
model.add(Conv2D(128, (3,3), strides=(2,2), padding='same'))
model.add(LeakyReLU(alpha=0.2))
# classifier
model.add(Flatten())
model.add(Dropout(0.4))
model.add(Dense(1, activation='sigmoid'))
# compile model
opt = Adam(lr=0.0002, beta_1=0.5)
model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])
return model
```
