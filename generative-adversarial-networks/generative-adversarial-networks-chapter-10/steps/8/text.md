
We will require one (or a half) batch of real images from the dataset each update to the
GAN model. A simple way to achieve this is to select a random sample of images from the
dataset each time. The generate real samples() function below implements this, taking the
prepared dataset as an argument, selecting and returning a random sample of digit images, and
their corresponding class label for the discriminator, specifically class = 1 indicating that they
are real images.

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
points required, and returning them as a batch of input samples for the generator model.

```
# generate points in latent space as input for the generator
def generate_latent_points(latent_dim, n_samples):
# generate points in the latent space
x_input = randn(latent_dim * n_samples)
# reshape into a batch of inputs for the network
x_input = x_input.reshape(n_samples, latent_dim)
return x_input
```
