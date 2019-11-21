We will train model now with real examples with a class label of one, and
randomly generated samples with a class label of zero. The development of these elements will
be useful later, and it helps to see that the discriminator is just a normal neural network model
for binary classification. First, we need a function to load and prepare the dataset of real images.
We will use the mnist.load data() function to load the MNIST dataset and just use the input
part of the training dataset as the real images.

```
# load mnist dataset
(trainX, _), (_, _) = load_data()
```

The images are 2D arrays of pixels and convolutional neural networks expect 3D arrays of
images as input, where each image has one or more channels We must update the images to have
an additional dimension for the grayscale channel. We can do this using the expand dims()
NumPy function and specify the final dimension for the channels-last image format.

```
# expand to 3d, e.g. add channels dimension
X = expand_dims(trainX, axis=-1)
```
