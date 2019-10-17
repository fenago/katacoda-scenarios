

The pixel values in images must be scaled prior to providing the images as input to a deep
learning neural network model during the training or evaluation of the model. Traditionally, the
images would have to be scaled prior to the development of the model and stored in memory or
on disk in the scaled format. An alternative approach is to scale the images using a preferred
scaling technique just-in-time during the training or model evaluation process. Keras supports
this type of data preparation for image data via the ImageDataGenerator class and API.

In this tutorial, you will discover how to use the ImageDataGenerator class to scale pixel
data just-in-time when fitting and evaluating deep learning neural network models. After
completing this tutorial, you will know:
- How to configure and a use the ImageDataGenerator class for train, validation, and test
datasets of images.
- How to use the ImageDataGenerator to normalize pixel values for a train and test image
dataset.
- How to use the ImageDataGenerator to center and standardize pixel values for a train
and test image dataset.

Let’s get started.