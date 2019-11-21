We will require one batch (or a half batch) of real images from the dataset each update to
the GAN model. A simple way to achieve this is to select a random sample of images from the
dataset each time. The generate real samples() function below implements this, taking the
prepared dataset as an argument, selecting and returning a random sample of images and their
corresponding label for the critic, specifically target = −1 indicating that they are real images.

```
# select real samples16.5. How to Train a Wasserstein GAN Model 317
def generate_real_samples(dataset, n_samples):
# choose random instances
ix = randint(0, dataset.shape[0], n_samples)
# select images
X = dataset[ix]
# generate class labels, -1 for 'real'
y = -ones((n_samples, 1))
return X, y
```
