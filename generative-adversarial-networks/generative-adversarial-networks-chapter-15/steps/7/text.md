
We can then define a function to retrieve a batch of randomly selected images from the training
dataset. The real images are returned with corresponding target values for the discriminator
model, e.g. y=1.0, to indicate they are real.

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

Next, we can develop the corresponding functions for the generator. First, a function for
generating random points in the latent space to use as input for generating images via the
generator model.

```
# generate points in latent space as input for the generator
def generate_latent_points(latent_dim, n_samples):
# generate points in the latent space
x_input = randn(latent_dim * n_samples)
# reshape into a batch of inputs for the network
x_input = x_input.reshape(n_samples, latent_dim)
return x_input
```
S
