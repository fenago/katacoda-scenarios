We can use the saved generator model to create new images on demand. This can be achieved
by first selecting a final model based on image quality, then loading it and providing new points
from the latent space as input in order to generate new plausible images from the domain. In
this case, we will use the model saved after 20 epochs, or 18,740 (60000 64 or 937 batches per epoch
×20 epochs) training iterations.

```
# example of loading the generator model and generating images
from keras.models import load_model
from numpy.random import randn
from matplotlib import pyplot
# generate points in latent space as input for the generator
def generate_latent_points(latent_dim, n_samples):
# generate points in the latent space
x_input = randn(latent_dim * n_samples)
# reshape into a batch of inputs for the network
x_input = x_input.reshape(n_samples, latent_dim)
return x_input
# create a plot of generated images (reversed grayscale)
def plot_generated(examples, n):
# plot images
for i in range(n * n):
# define subplot
pyplot.subplot(n, n, 1 + i)
# turn off axis
pyplot.axis('off')
# plot raw pixel data
pyplot.imshow(examples[i, :, :, 0], cmap='gray_r')
pyplot.show()
# load model
model = load_model('model_018740.h5')
# generate images
latent_points = generate_latent_points(100, 100)
# generate images
X = model.predict(latent_points)
# plot the result
plot_generated(X, 10)
```

Running the example generates a plot of 10 × 10, or 100, new and plausible handwritten
digits.