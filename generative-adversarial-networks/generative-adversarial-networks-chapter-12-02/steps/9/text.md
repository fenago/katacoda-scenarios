
We can test the calculation of the inception score on some real images. The Keras API
provides access to the CIFAR-10 dataset (described in Section 8.2). These are color photos
with the small size of 32 × 32 pixels. First, we can split the images into groups, then upsample
the images to the expected size of 299 × 299, pre-process the pixel values, predict the class
probabilities, then calculate the inception score. This will be a useful example if you intend to
calculate the inception score on your own generated images, as you may have to either scale
the images to the expected size for the inception v3 model or change the model to perform the
upsampling for you. First, the images can be loaded and shuffled to ensure each split covers a
diverse set of classes.

```
...
# load cifar10 images
(images, _), (_, _) = cifar10.load_data()
# shuffle images
shuffle(images)
```

Next, we need a way to scale the images. We will use the scikit-image library to resize
the NumPy array of pixel values to the required size. The scale images() function below
implements this.

```
# scale an array of images to a new size
def scale_images(images, new_shape):
images_list = list()
for image in images:
# resize with nearest neighbor interpolation
new_image = resize(image, new_shape, 0)
# store
images_list.append(new_image)
return asarray(images_list)
```

You may have to install the scikit-image library if it is not already installed. This can be
achieved as follows:

`pip install scikit-image`
