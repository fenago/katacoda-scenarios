
This model can then be used to predict the feature vector for one or more images. Our
images are likely to not have the required shape. We will use the scikit-image library to resize
the NumPy array of pixel values to the required size. The scale images() function below
implements this.

```
# scale an array of images to a new size
def scale_images(images, new_shape):13.5. How to Implement the FID With Keras 272
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

```
pip install scikit-image
```
