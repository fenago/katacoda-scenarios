We could start training this model now with real examples with a class label of one and
randomly generate samples with a class label of zero. The development of these elements will be
useful later, and it helps to see that the discriminator is just a normal neural network model for
binary classification. First, we need a function to load and prepare the dataset of real images.
We will use the cifar.load data() function to load the CIFAR-10 dataset and just use the
input part of the training dataset as the real images.

```
...
# load cifar10 dataset
(trainX, _), (_, _) = load_data()
```

We must scale the pixel values from the range of unsigned integers in [0,255] to the normalized
range of [-1,1]. The generator model will generate images with pixel values in the range [-1,1] as
it will use the Tanh activation function, a best practice. It is also a good practice for the real
images to be scaled to the same range.

```
...
# convert from unsigned ints to floats
X = trainX.astype('float32')
# scale from [0,255] to [-1,1]
X = (X - 127.5) / 127.5
```

The load real samples() function below implements the loading and scaling of real CIFAR-
10 photographs.

```
# load and prepare cifar10 training images
def load_real_samples():
# load cifar10 dataset
(trainX, _), (_, _) = load_data()
# convert from unsigned ints to floats
X = trainX.astype('float32')
# scale from [0,255] to [-1,1]
X = (X - 127.5) / 127.5
return X
```

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

Finally, we need to train the discriminator model. This involves repeatedly retrieving samples
of real images and samples of generated images and updating the model for a fixed number of
iterations. We will ignore the idea of epochs for now (e.g. complete passes through the training
dataset) and fit the discriminator model for a fixed number of batches. The model will learn to
discriminate between real and fake (randomly generated) images rapidly, therefore not many
batches will be required before it learns to discriminate perfectly.
The train discriminator() function implements this, using a batch size of 128 images,
where 64 are real and 64 are fake each iteration. We update the discriminator separately for
real and fake examples so that we can calculate the accuracy of the model on each sample prior
to the update. This gives insight into how the discriminator model is performing over time.

```
# train the discriminator model
def train_discriminator(model, dataset, n_iter=20, n_batch=128):
half_batch = int(n_batch / 2)
# manually enumerate epochs
for i in range(n_iter):
# get randomly selected 'real' samples
X_real, y_real = generate_real_samples(dataset, half_batch)
# update discriminator on real samples
_, real_acc = model.train_on_batch(X_real, y_real)
# generate 'fake' examples
X_fake, y_fake = generate_fake_samples(half_batch)
# update discriminator on fake samples
_, fake_acc = model.train_on_batch(X_fake, y_fake)
# summarize performance
print('>%d real=%.0f%% fake=%.0f%%' % (i+1, real_acc*100, fake_acc*100))
```

Tying all of this together, the complete example of training an instance of the discriminator
model on real and randomly generated (fake) images is listed below.