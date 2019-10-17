The first step is to download the pre-trained model weights. These were trained using the
DarkNet code base on the MSCOCO dataset. Download the model weights and place them
into your current working directory with the filename yolov3.weights. It is a large file (237
megabytes) and may take a moment to download depending on the speed of your internet
connection.

`wget https://pjreddie.com/media/files/yolov3.weights`{{execute}}

Next, we need to define a Keras model that has the right number and type of layers to
match the downloaded model weights. The model architecture is called DarkNet and was
originally loosely based on the VGG-16 model. The yolo3 one file to detect them all.py
script provides the make yolov3 model() function to create the model for us, and the helper
function conv block() that is used to create blocks of layers. These two functions can be
copied directly from the script. We can now define the Keras model for YOLOv3.

```
# define the model
model = make_yolov3_model()
```

Next, we need to load the model weights. The model weights are stored in whatever format
that was used by DarkNet. Rather than trying to decode the file manually, we can use the
WeightReader class provided in the script. To use the WeightReader, it is instantiated with
the path to our weights file (e.g. yolov3.weights). This will parse the file and load the model
weights into memory in a format that we can set into our Keras model.

```
# load the model weights
weight_reader = WeightReader('yolov3.weights')
```

We can then call the load weights() function of the WeightReader instance, passing in
our defined Keras model to set the weights into the layers.


```
# set the model weights into the model
weight_reader.load_weights(model)
```

That’s it; we now have a YOLOv3 model for use. We can save this model to a Keras
compatible .h5 model file ready for later use.

```
# save the model to file
model.save('model.h5')
```
We can tie all of this together; the complete code example including functions copied directly
from the yolo3 one file to detect them all is already written in `01_save_model.py` file.