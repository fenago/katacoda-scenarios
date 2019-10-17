There are conventions for storing and structuring your image dataset on disk in order to make
it fast and efficient to load and when training and evaluating deep learning models. Once
structured, you can use tools like the ImageDataGenerator class in the Keras deep learning
library to automatically load your train, test, and validation datasets. In addition, the generator
will progressively load the images in your dataset (e.g. just-in-time), allowing you to work with
both small and very large datasets containing thousands or millions of images that may not fit
into system memory. In this tutorial, you will discover how to structure an image dataset and
how to load it progressively when fitting and evaluating a deep learning model. 

After completing this tutorial, you will know:
- How to organize train, validation, and test image datasets into a consistent directory
structure.
- How to use the ImageDataGenerator class to progressively load the images for a given
dataset.
- How to use a prepared data generator to train, evaluate, and make predictions with a
deep learning model.

Let’s get started