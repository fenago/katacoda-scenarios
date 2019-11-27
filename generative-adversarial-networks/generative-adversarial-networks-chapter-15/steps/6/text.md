
The generator model is updated via the discriminator model. This is achieved by creating
a composite model that stacks the generator on top of the discriminator so that error signals
can flow back through the discriminator to the generator. The weights of the discriminator are
marked as not trainable when used in this composite model. Updates via the composite model
involve using the generator to create new images by providing random points in the latent space
as input. The generated images are passed to the discriminator, which will classify them as
real or fake. The weights are updated as though the generated images are real (e.g. target
of 1.0), allowing the generator to be updated toward generating more realistic images. The
define gan() function defines and compiles the composite model for updating the generator
model via the discriminator, again optimized via mean squared error as per the LSGAN.

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
# compile model with L2 loss
model.compile(loss='mse', optimizer=Adam(lr=0.0002, beta_1=0.5))
return model
```


Next, we can define a function to load the MNIST handwritten digit dataset and scale the
pixel values to the range [-1,1] to match the images output by the generator model. Only the
training part of the MNIST dataset is used, which contains 60,000 centered grayscale images of
digits zero through nine.

```
# load mnist images
def load_real_samples():
# load dataset
(trainX, _), (_, _) = load_data()
# expand to 3d, e.g. add channels
X = expand_dims(trainX, axis=-1)
# convert from ints to floats15.3. How to Develop an LSGAN for MNIST 293
X = X.astype('float32')
# scale from [0,255] to [-1,1]
X = (X - 127.5) / 127.5
return X
```
