We need a new photo for object detection, ideally with object classes that we know that the
model can recognize from the MSCOCO dataset. We will use a photograph of three zebras
taken by Boegh4, and released under a permissive license.


The photograph has been placed in your current working directory with the filename `zebra.jpg`.

#### Code
Making a prediction is straightforward, although interpreting the prediction requires some
work. The first step is to load the YOLOv3 Keras model. This might be the slowest part of
making a prediction.

```
# load yolov3 model
model = load_model(model.h5)
```


Next, we need to load our new photograph and prepare it as suitable input to the model.
The model expects inputs to be color images with the square shape of 416 x 416 pixels. We can
use the load img() Keras function to load the image and the target size argument to resize
the image after loading. We can also use the img to array() function to convert the loaded
PIL image object into a NumPy array, and then rescale the pixel values from 0-255 to 0-1 32-bit
floating point values.

```
# load the image with the required size
image = load_img(zebra.jpg, target_size=(416, 416))
# convert to numpy array
image = img_to_array(image)
# scale pixel values to [0, 1]
image = image.astype(float32)
image /= 255.0
```
