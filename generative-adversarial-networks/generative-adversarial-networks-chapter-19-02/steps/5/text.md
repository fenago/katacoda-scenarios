
We will require one batch (or a half batch) of real images from the dataset each update to
the GAN model. A simple way to achieve this is to select a random sample of images from the
dataset each time. The generate real samples() function below implements this, taking the
prepared dataset as an argument, selecting and returning a random sample of Fashion-MNIST
images and clothing class labels. The dataset argument provided to the function is a list
comprised of the images and class labels as returned from the load real samples() function.
The function also returns their corresponding class label for the discriminator, specifically
class = 1 indicating that they are real images.

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
