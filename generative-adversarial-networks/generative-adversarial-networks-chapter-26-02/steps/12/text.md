
Each training iteration we will require a sample of real images from each domain as input to
the discriminator and composite generator models. This can be achieved by selecting a random
batch of samples. The generate real samples() function below implements this, taking a
NumPy array for a domain as input and returning the requested number of randomly selected
images, as well as the target for the PatchGAN discriminator model indicating the images are
real (target = 1.0). As such, the shape of the PatchGAN output is also provided, which in the
case of 256×256 images will be 16, or a 16×16×1 activation map, defined by the patch shape
function argument.

```
# select a batch of random samples, returns images and target
def generate_real_samples(dataset, n_samples, patch_shape):
# choose random instances
ix = randint(0, dataset.shape[0], n_samples)
# retrieve selected images
X = dataset[ix]
# generate 'real' class labels (1)
y = ones((n_samples, patch_shape, patch_shape, 1))
return X, y
```
