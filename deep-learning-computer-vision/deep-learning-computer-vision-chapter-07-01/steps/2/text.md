This tutorial is divided into following parts; they are:
1. MNIST Handwritten Image Classification Dataset.
2. ImageDataGenerator Class for Pixel Scaling
3. How to Normalize Images With ImageDataGenerator


#### MNIST Handwritten Image Classification Dataset
Before we dive into the usage of the ImageDataGenerator class for preparing image data, we
must select an image dataset on which to test the generator. The MNIST problem, is an image
classification problem comprised of 70,000 images of handwritten digits. The goal of the problem
is to classify a given image of a handwritten digit as an integer from 0 to 9. As such, it is a
multiclass image classification problem.

This dataset is provided as part of the Keras library and can be automatically downloaded (if
needed) and loaded into memory by a call to the keras.datasets.mnist.load data() function.
The function returns two tuples: one for the training inputs and outputs and one for the test
inputs and outputs. Note, if this is the first time using the MNIST dataset in Keras, the dataset
will be downloaded and placed in the .keras/datasets/ directory in your home directory. The
dataset is only 11 megabytes and will download very quickly.

```
# example of loading the MNIST dataset
from keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
```
