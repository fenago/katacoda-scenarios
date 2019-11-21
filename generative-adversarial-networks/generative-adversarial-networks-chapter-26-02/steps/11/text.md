
We need to create a composite model for each generator model, e.g. the Generator-A (BtoA)
for zebra to horse translation, and the Generator-B (AtoB) for horse to zebra translation. All
of this forward and backward across two domains gets confusing. Below is a complete listing
of all of the inputs and outputs for each of the composite models. Identity and cycle loss
are calculated as the L1 distance between the input and output image for each sequence of
translations. Adversarial loss is calculated as the L2 distance between the model output and
the target values of 1.0 for real and 0.0 for fake. Defining the models is the hard part of the
CycleGAN; the rest is standard GAN training and is relatively straightforward. Next, we can
load our paired images dataset in compressed NumPy array format. This will return a list of
two NumPy arrays: the first for source images and the second for corresponding target images.

```
# load and prepare training images
def load_real_samples(filename):
# load the dataset
data = load(filename)
# unpack arrays
X1, X2 = data['arr_0'], data['arr_1']
# scale from [0,255] to [-1,1]
X1 = (X1 - 127.5) / 127.5
X2 = (X2 - 127.5) / 127.5
return [X1, X2]
```
