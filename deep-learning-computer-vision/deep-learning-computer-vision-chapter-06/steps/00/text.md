
This tutorial is divided into five parts; they are:
1. Test Image
2. Keras Image Processing API
3. How to Load an Image With Keras
4. How to Convert an Image With Keras
5. How to Save an Image With Keras


#### Keras Image Processing API
The Keras deep learning library provides utilities for working with image data. The main API
is the ImageDataGenerator class that combines data loading, preparation, and augmentation.
We will not cover the ImageDataGenerator class in this tutorial. Instead, we will take a closer
look at a few less-documented or undocumented functions that may be useful when working
with image data and modeling with the Keras API. Specifically, Keras provides functions for
loading, converting, and saving image data. The functions are in the utils.py function and
exposed via the image.py module. These functions can be useful convenience functions when
getting started on a new deep learning computer vision project or when you need to inspect
specific images.

Some of these functions are demonstrated when working with pre-trained models in the
Applications section of the API documentation. All image handling in Keras requires that the
Pillow library is installed. Let’s take a closer look at each of these functions in turn.