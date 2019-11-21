How to Develop a Semi-Supervised GAN for MNIST
In this section, we will develop a semi-supervised GAN model for the MNIST handwritten digit
dataset (described in Section 7.2). The dataset has 10 classes for the digits 0-9, therefore the
classifier model will have 10 output nodes. The model will be fit on the training dataset that
contains 60,000 examples. Only 100 of the images in the training dataset will be used with20.4. How to Develop a Semi-Supervised GAN for MNIST 436
labels, 10 from each of the 10 classes. We will start off by defining the models. We will use the
stacked discriminator model, exactly as defined in the previous section. Next, we can define
the generator model. In this case, the generator model will take as input a point in the latent
space and will use transpose convolutional layers to output a 28 × 28 grayscale image. The
define generator() function below implements this and returns the defined generator model.

```
# define the standalone generator model
def define_generator(latent_dim):
# image generator input
in_lat = Input(shape=(latent_dim,))
# foundation for 7x7 image
n_nodes = 128 * 7 * 7
gen = Dense(n_nodes)(in_lat)
gen = LeakyReLU(alpha=0.2)(gen)
gen = Reshape((7, 7, 128))(gen)
# upsample to 14x14
gen = Conv2DTranspose(128, (4,4), strides=(2,2), padding='same')(gen)
gen = LeakyReLU(alpha=0.2)(gen)
# upsample to 28x28
gen = Conv2DTranspose(128, (4,4), strides=(2,2), padding='same')(gen)
gen = LeakyReLU(alpha=0.2)(gen)
# output
out_layer = Conv2D(1, (7,7), activation='tanh', padding='same')(gen)
# define model
model = Model(in_lat, out_layer)
return model
```
