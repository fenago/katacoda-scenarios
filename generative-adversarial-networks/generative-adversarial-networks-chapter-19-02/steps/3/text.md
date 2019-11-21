Unconditional GAN for Fashion-MNIST
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

The generator model takes as input a point in the latent space and outputs a single 28 × 28
grayscale image. This is achieved by using a fully connected layer to interpret the point in the
latent space and provide sufficient activations that can be reshaped into many copies (in this
case 128) of a low-resolution version of the output image (e.g. 7 × 7). This is then upsampled
twice, doubling the size and quadrupling the area of the activations each time using transpose
convolutional layers. The model uses best practices such as the LeakyReLU activation, a kernel
size that is a factor of the stride size, and a hyperbolic tangent (Tanh) activation function in
the output layer.

The define generator() function below defines the generator model, but intentionally does
not compile it as it is not trained directly, then returns the model. The size of the latent space
is parameterized as a function argument.

```
# define the standalone generator model
def define_generator(latent_dim):
model = Sequential()
# foundation for 7x7 image
n_nodes = 128 * 7 * 7
model.add(Dense(n_nodes, input_dim=latent_dim))
model.add(LeakyReLU(alpha=0.2))
model.add(Reshape((7, 7, 128)))
# upsample to 14x14
model.add(Conv2DTranspose(128, (4,4), strides=(2,2), padding='same'))
model.add(LeakyReLU(alpha=0.2))
# upsample to 28x28
model.add(Conv2DTranspose(128, (4,4), strides=(2,2), padding='same'))
model.add(LeakyReLU(alpha=0.2))
# generate
model.add(Conv2D(1, (7,7), activation='tanh', padding='same'))
return model
```

Next, a GAN model can be defined that combines both the generator model and the
discriminator model into one larger model. This larger model will be used to train the model
weights in the generator, using the output and error calculated by the discriminator model. The
discriminator model is trained separately, and as such, the model weights are marked as not
trainable in this larger GAN model to ensure that only the weights of the generator model are
updated. This change to the trainability of the discriminator weights only has an effect when
training the combined GAN model, not when training the discriminator standalone.
This larger GAN model takes as input a point in the latent space, uses the generator model
to generate an image which is fed as input to the discriminator model, then is output or classified
as real or fake. The define gan() function below implements this, taking the already-defined
generator and discriminator models as input.

```
# define the combined generator and discriminator model, for updating the generator
def define_gan(generator, discriminator):
# make weights in the discriminator not trainable
discriminator.trainable = False
# connect them
model = Sequential()
# add generator
model.add(generator)
# add the discriminator
model.add(discriminator)
# compile model
opt = Adam(lr=0.0002, beta_1=0.5)
model.compile(loss='binary_crossentropy', optimizer=opt)
return model
```

Now that we have defined the GAN model, we need to train it. But, before we can train the
model, we require input data. The first step is to load and prepare the Fashion-MNIST dataset.
We only require the images in the training dataset. The images are black and white, therefore
we must add an additional channel dimension to transform them to be three dimensional, as
expected by the convolutional layers of our models. Finally, the pixel values must be scaled to
the range [-1,1] to match the output of the generator model. The load real samples() function
below implements this, returning the loaded and scaled Fashion-MNIST training dataset ready
for modeling.

```
# load fashion mnist images
def load_real_samples():
# load dataset
(trainX, _), (_, _) = load_data()
# expand to 3d, e.g. add channels
X = expand_dims(trainX, axis=-1)
# convert from ints to floats
X = X.astype('float32')
# scale from [0,255] to [-1,1]
X = (X - 127.5) / 127.5
return X
```

We will require one batch (or a half batch) of real images from the dataset each update to
the GAN model. A simple way to achieve this is to select a random sample of images from the
dataset each time. The generate real samples() function below implements this, taking the
prepared dataset as an argument, selecting and returning a random sample of Fashion-MNIST17.4. Unconditional GAN for Fashion-MNIST 341
images and their corresponding class label for the discriminator, specifically class = 1, indicating
that they are real images.

```
# select real samples
def generate_real_samples(dataset, n_samples):
# choose random instances
ix = randint(0, dataset.shape[0], n_samples)
# select images
X = dataset[ix]
# generate class labels
y = ones((n_samples, 1))
return X, y
```

Next, we need inputs for the generator model. These are random points from the latent
space, specifically Gaussian distributed random variables. The generate latent points()
function implements this, taking the size of the latent space as an argument and the number of
points required and returning them as a batch of input samples for the generator model.

```
# generate points in latent space as input for the generator
def generate_latent_points(latent_dim, n_samples):
# generate points in the latent space
x_input = randn(latent_dim * n_samples)
# reshape into a batch of inputs for the network
x_input = x_input.reshape(n_samples, latent_dim)
return x_input
```

Next, we need to use the points in the latent space as input to the generator in order to
generate new images. The generate fake samples() function below implements this, taking
the generator model and size of the latent space as arguments, then generating points in the
latent space and using them as input to the generator model. The function returns the generated
images and their corresponding class label for the discriminator model, specifically class = 0 to
indicate they are fake or generated.


```
# use the generator to generate n fake examples, with class labels
def generate_fake_samples(generator, latent_dim, n_samples):
# generate points in latent space
x_input = generate_latent_points(latent_dim, n_samples)
# predict outputs
X = generator.predict(x_input)
# create class labels
y = zeros((n_samples, 1))
return X, y
```

We are now ready to fit the GAN models. The model is fit for 100 training epochs, which is
arbitrary, as the model begins generating plausible items of clothing after perhaps 20 epochs. A
batch size of 128 samples is used, and each training epoch involves 60000 128 , or about 468 batches
of real and fake samples and updates to the model. First, the discriminator model is updated
for a half batch of real samples, then a half batch of fake samples, together forming one batch of
weight updates. The generator is then updated via the composite GAN model. Importantly, the
class label is set to 1 or real for the fake samples. This has the effect of updating the generator
toward getting better at generating real samples on the next batch. The train() function
below implements this, taking the defined models, dataset, and size of the latent dimension as
arguments and parameterizing the number of epochs and batch size with default arguments.
The generator model is saved at the end of training.

```
# train the generator and discriminator
def train(g_model, d_model, gan_model, dataset, latent_dim, n_epochs=100, n_batch=128):
bat_per_epo = int(dataset.shape[0] / n_batch)
half_batch = int(n_batch / 2)
# manually enumerate epochs
for i in range(n_epochs):
# enumerate batches over the training set
for j in range(bat_per_epo):
# get randomly selected 'real' samples
X_real, y_real = generate_real_samples(dataset, half_batch)
# update discriminator model weights
d_loss1, _ = d_model.train_on_batch(X_real, y_real)
# generate 'fake' examples
X_fake, y_fake = generate_fake_samples(g_model, latent_dim, half_batch)
# update discriminator model weights
d_loss2, _ = d_model.train_on_batch(X_fake, y_fake)
# prepare points in latent space as input for the generator
X_gan = generate_latent_points(latent_dim, n_batch)
# create inverted labels for the fake samples
y_gan = ones((n_batch, 1))
# update the generator via the discriminator's error
g_loss = gan_model.train_on_batch(X_gan, y_gan)
# summarize loss on this batch
print('>%d, %d/%d, d1=%.3f, d2=%.3f g=%.3f' %
(i+1, j+1, bat_per_epo, d_loss1, d_loss2, g_loss))
# save the generator model
g_model.save('generator.h5')
```

We can then define the size of the latent space, define all three models, and train them on
the loaded Fashion-MNIST dataset.

```
...
# size of the latent space
latent_dim = 100
# create the discriminator
discriminator = define_discriminator()
# create the generator
generator = define_generator(latent_dim)
# create the gan
gan_model = define_gan(generator, discriminator)
# load image data
dataset = load_real_samples()
# train model
train(generator, discriminator, gan_model, dataset, latent_dim)
```