We will want to show the original photo again later, which means we will need to scale the
bounding boxes of all detected objects from the square shape back to the original shape. As
such, we can load the image and retrieve the original shape.

```
# load the image to get its shape
image = load_img('zebra.jpg')
width, height = image.size
```

We can tie all of this together into a convenience function named load image pixels()
that takes the filename and target size and returns the scaled pixel data ready to provide as
input to the Keras model, as well as the original width and height of the image.

```
# load and prepare an image
def load_image_pixels(filename, shape):
# load the image to get its shape
image = load_img(filename)
width, height = image.size
# load the image with the required size
image = load_img(filename, target_size=shape)
# convert to numpy array
image = img_to_array(image)
# scale pixel values to [0, 1]
image = image.astype('float32')
image /= 255.0
# add a dimension so that we have one sample24.4. Object Detection With YOLOv3 378
image = expand_dims(image, 0)
return image, width, height
```

We can then call this function to load our photo of zebras.

```
# define the expected input shape for the model
input_w, input_h = 416, 416
# define our new photo
photo_filename = 'zebra.jpg'
# load and prepare image
image, image_w, image_h = load_image_pixels(photo_filename, (input_w, input_h))
```
Listing 24.11: Example of calling a function to prepare an image for making a prediction.
We can now feed the photo into the Keras model and make a prediction.

```
# make prediction
yhat = model.predict(image)
# summarize the shape of the list of arrays
print([a.shape for a in yhat])
```

That’s it, at least for making a prediction. 