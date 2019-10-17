The VGG16 model was developed by the Visual Graphics Group (VGG) at Oxford and was
described in the 2014 paper titled Very Deep Convolutional Networks for Large-Scale
Image Recognition. By default, the model expects color input images to be rescaled to the
size of 224 x 224 squares. The model can be loaded as follows:

```
# example of loading the vgg16 model
from keras.applications.vgg16 import VGG16
# load model
model = VGG16()
# summarize the model
model.summary()
```

We can run the centering code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_18/01_vgg_model.py` to view file.


#### Run Code
Now, run the python code by running: `python 01_vgg_model.py`{{execute}}


Running the example will load the VGG16 model and download the model weights if required.
The model can then be used directly to classify a photograph into one of 1,000 classes. In this
case, the model architecture is summarized to confirm that it was loaded correctly.