
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
prepared dataset as an argument, selecting and returning a random sample of Fashion-MNIST
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
