Color images have height, width, and color channel dimensions. When represented as threedimensional arrays, the channel dimension for the image data is last by default, but may be
moved to be the first dimension, often for performance-tuning reasons. The use of these two
channel ordering formats and preparing data to meet a specific preferred channel ordering can
be confusing to beginners. In this tutorial, you will discover channel ordering formats, how
to prepare and manipulate image data to meet formats, and how to configure the Keras deep
learning library for different channel orderings. After completing this tutorial, you will know:
- The three-dimensional array structure of images and the channels first and channels last
array formats.
- How to add a channels dimension and how to convert images between the channel formats.
- How the Keras deep learning library manages a preferred channel ordering and how to
change and query this preference.
Let’s get started.
