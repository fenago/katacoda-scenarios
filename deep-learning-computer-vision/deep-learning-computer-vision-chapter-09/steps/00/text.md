This tutorial is divided into eight parts; they are:
1. Image Data Augmentation
2. Sample Image
3. Image Augmentation With ImageDataGenerator
4. Horizontal and Vertical Shift Augmentation
5. Horizontal and Vertical Flip Augmentation
6. Random Rotation Augmentation
7. Random Brightness Augmentation
8. Random Zoom Augmentation



#### Image Data Augmentation
The performance of deep learning neural networks often improves with the amount of data
available. Data augmentation is a technique to artificially create new training data from existing
training data. This is done by applying domain-specific techniques to examples from the training
data that create new and different training examples. Image data augmentation is perhaps
the most well-known type of data augmentation and involves creating transformed versions of
images in the training dataset that belong to the same class as the original image. Transforms
include a range of operations from the field of image manipulation, such as shifts, flips, zooms,
and much more.

Modern deep learning algorithms, such as the convolutional neural network, or CNN, can
learn features that are invariant to their location in the image. Nevertheless, augmentation can
further aid in this transform-invariant approach to learning and can aid the model in learning
features that are also invariant to transforms such as left-to-right to top-to-bottom ordering,
light levels in photographs, and more. Image data augmentation is typically only applied to
the training dataset, and not to the validation or test dataset. This is different from data
preparation such as image resizing and pixel scaling; they must be performed consistently across
all datasets that interact with the model.