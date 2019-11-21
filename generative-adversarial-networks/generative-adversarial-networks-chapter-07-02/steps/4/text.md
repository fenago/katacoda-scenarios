
Finally, we must scale the pixel values from the range of unsigned integers in [0,255] to the
normalized range of [0,1]. It is best practice to use the range [-1,1], but in this case the range
[0,1] works just fine.

```
# convert from unsigned ints to floats
X = X.astype('float32')
# scale from [0,255] to [0,1]
X = X / 255.0
```

The load real samples() function below implements this.

```
# load and prepare mnist training images
def load_real_samples():
# load mnist dataset
(trainX, _), (_, _) = load_data()
# expand to 3d, e.g. add channels dimension
X = expand_dims(trainX, axis=-1)
# convert from unsigned ints to floats
X = X.astype('float32')
# scale from [0,255] to [0,1]
X = X / 255.0
return X
```

The model will be updated in batches, specifically with a collection of real samples and a
collection of generated samples. On training, an epoch is defined as one pass through the entire
training dataset. We could systematically enumerate all samples in the training dataset, and
that is a good approach, but good training via stochastic gradient descent requires that the
training dataset be shuffled prior to each epoch. A simpler approach is to select random samples
of images from the training dataset. The generate real samples() function below will take
the training dataset as an argument and will select a random subsample of images; it will also
return class labels for the sample, specifically a class label of 1, to indicate real images.

```
# select real samples
def generate_real_samples(dataset, n_samples):
# choose random instances
ix = randint(0, dataset.shape[0], n_samples)
# retrieve selected images
X = dataset[ix]
# generate 'real' class labels (1)
y = ones((n_samples, 1))
return X, y
```
