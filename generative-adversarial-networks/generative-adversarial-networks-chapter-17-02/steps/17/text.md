In this section, we will use the trained generator model to conditionally generate new photos of
items of clothing. We can update our code example for generating new images with the model
to now generate images conditional on the class label. We can generate 10 examples for each
class label in columns. The complete example is listed below.

```
# example of loading the generator model and generating images
from numpy import asarray
from numpy.random import randn
from numpy.random import randint
from keras.models import load_model
from matplotlib import pyplot
# generate points in latent space as input for the generator
def generate_latent_points(latent_dim, n_samples, n_classes=10):
# generate points in the latent space
x_input = randn(latent_dim * n_samples)
# reshape into a batch of inputs for the network
z_input = x_input.reshape(n_samples, latent_dim)
# generate labels
labels = randint(0, n_classes, n_samples)
return [z_input, labels]
# create and save a plot of generated images
def save_plot(examples, n):
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
model = load_model('cgan_generator.h5')
# generate images
latent_points, labels = generate_latent_points(100, 100)
# specify labels
labels = asarray([x for _ in range(10) for x in range(10)])
# generate images
X = model.predict([latent_points, labels])
# scale from [-1,1] to [0,1]
X = (X + 1) / 2.0
# plot the result
save_plot(X, 10)
```

Running the example loads the saved conditional GAN model and uses it to generate 100
items of clothing. The clothing is organized in columns. From left to right, they are t-shirt,
trouser, pullover, dress, coat, sandal, shirt, sneaker, bag, and ankle boot. We can see not only are
the randomly generated items of clothing plausible, but they also match their expected category.

![](https://github.com/fenago/katacoda-scenarios/raw/master/generative-adversarial-networks/generative-adversarial-networks-chapter-17-02/steps/17/1.png)
