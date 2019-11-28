
Next, we can load our paired images dataset in compressed NumPy array format. This will
return a list of two NumPy arrays: the first for source images and the second for corresponding
target images.

```
# load and prepare training images
def load_real_samples(filename):
# load the compressed arrays
data = load(filename)
# unpack the arrays
X1, X2 = data['arr_0'], data['arr_1']
# scale from [0,255] to [-1,1]
X1 = (X1 - 127.5) / 127.5
X2 = (X2 - 127.5) / 127.5
return [X1, X2]
```

Training the discriminator will require batches of real and fake images. The generate real samples()
function below will prepare a batch of random pairs of images from the training dataset, and
the corresponding discriminator label of class = 1 to indicate they are real.

```
# select a batch of random samples, returns images and target
def generate_real_samples(dataset, n_samples, patch_shape):
# unpack dataset
trainA, trainB = dataset
# choose random instances
ix = randint(0, trainA.shape[0], n_samples)
# retrieve selected images
X1, X2 = trainA[ix], trainB[ix]
# generate 'real' class labels (1)
y = ones((n_samples, patch_shape, patch_shape, 1))
return [X1, X2], y
```
