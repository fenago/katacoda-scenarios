
The discriminator model will be updated in batches, specifically with a collection of real
samples and a collection of generated samples. On training, an epoch is defined as one pass
through the entire training dataset. We could systematically enumerate all samples in the
training dataset, and that is a good approach, but good training via stochastic gradient descent
requires that the training dataset be shuffled prior to each epoch. A simpler approach is to
select random samples of images from the training dataset. The generate real samples()
function below will take the training dataset as an argument and will select a random subsample
of images; it will also return class labels for the sample, specifically a class label of 1, to indicate
real images.

```
# select real samples
def generate_real_samples(dataset, n_samples):
# choose random instances8.3. How to Define and Train the Discriminator Model 140
ix = randint(0, dataset.shape[0], n_samples)
# retrieve selected images
X = dataset[ix]
# generate 'real' class labels (1)
y = ones((n_samples, 1))
return X, y
```

Now, we need a source of fake images. We don’t have a generator model yet, so instead, we can
generate images comprised of random pixel values, specifically random pixel values in the range
[0,1], then scaled to the range [-1, 1] like our scaled real images. The generate fake samples()
function below implements this behavior and generates images of random pixel values and their
associated class label of 0, for fake.

```
# generate n fake samples with class labels
def generate_fake_samples(n_samples):
# generate uniform random numbers in [0,1]
X = rand(32 * 32 * 3 * n_samples)
# update to have the range [-1, 1]
X = -1 + X * 2
# reshape into a batch of color images
X = X.reshape((n_samples, 32, 32, 3))
# generate 'fake' class labels (0)
y = zeros((n_samples, 1))
return X, y
```
