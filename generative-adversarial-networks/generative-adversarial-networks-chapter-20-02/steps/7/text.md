
Next, we can define a function for retrieving a batch of real training examples. A sample
of images and labels is selected, with replacement. This same function can be used to retrieve
examples from the labeled and unlabeled dataset, later when we train the models. In the case
of the unlabeled dataset, we will ignore the labels.

```
# select real samples
def generate_real_samples(dataset, n_samples):
# split into images and labels
images, labels = dataset
# choose random instances
ix = randint(0, images.shape[0], n_samples)
# select images and labels
X, labels = images[ix], labels[ix]
# generate class labels
y = ones((n_samples, 1))
return [X, labels], y
```

Next, we can define functions to help in generating images using the generator model. First,
the generate latent points() function will create a batch worth of random points in the
latent space that can be used as input for generating images. The generate fake samples()
function will call this function to generate a batch worth of images that can be fed to the
unsupervised discriminator model or the composite GAN model during training.

```
# generate points in latent space as input for the generator
def generate_latent_points(latent_dim, n_samples):
# generate points in the latent space
z_input = randn(latent_dim * n_samples)
# reshape into a batch of inputs for the network
z_input = z_input.reshape(n_samples, latent_dim)
return z_input
# use the generator to generate n fake examples, with class labels
def generate_fake_samples(generator, latent_dim, n_samples):
# generate points in latent space
z_input = generate_latent_points(latent_dim, n_samples)
# predict outputs
images = generator.predict(z_input)
# create class labels
y = zeros((n_samples, 1))
return images, y
```
