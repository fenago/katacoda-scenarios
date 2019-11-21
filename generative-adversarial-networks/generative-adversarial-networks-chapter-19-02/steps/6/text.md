
Next, we need inputs for the generator model. These are random points from the latent
space, specifically Gaussian distributed random variables. The generate latent points()
function implements this, taking the size of the latent space as an argument and the number of
points required, and returning them as a batch of input samples for the generator model. The
function also returns randomly selected integers in [0,9] inclusively for the 10 class labels in the
Fashion-MNIST dataset.

```
# generate points in latent space as input for the generator
def generate_latent_points(latent_dim, n_samples, n_classes=10):
# generate points in the latent space
x_input = randn(latent_dim * n_samples)
# reshape into a batch of inputs for the network
z_input = x_input.reshape(n_samples, latent_dim)
# generate labels
labels = randint(0, n_classes, n_samples)
return [z_input, labels]
```

Next, we need to use the points in the latent space and clothing class labels as input
to the generator in order to generate new images. The generate fake samples() function
below implements this, taking the generator model and size of the latent space as arguments,
then generating points in the latent space and using them as input to the generator model.
The function returns the generated images, their corresponding clothing class label, and their
discriminator class label, specifically class = 0 to indicate they are fake or generated.

```
# use the generator to generate n fake examples, with class labels
def generate_fake_samples(generator, latent_dim, n_samples):
# generate points in latent space
z_input, labels_input = generate_latent_points(latent_dim, n_samples)
# predict outputs
images = generator.predict([z_input, labels_input])
# create class labels
y = zeros((n_samples, 1))
return [images, labels_input], y
```
