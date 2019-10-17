The Residual Network, or ResNet for short, is a model that makes use of the residual module
involving shortcut connections. It was developed by researchers at Microsoft and described in
the 2015 paper titled Deep Residual Learning for Image Recognition. The model expects
color images to have the square shape 224 x 224.

```
# example of loading the resnet50 model
from keras.applications.resnet50 import ResNet50
# load model
model = ResNet50()
# summarize the model
model.summary()
```

We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_18/03_resnet_model.py` to view file.


#### Run Code
Now, run the python code by running: `python 03_resnet_model.py`{{execute}}


Running the example will load the model, downloading the weights if required, and then
summarize the model architecture to confirm it was loaded correctly. The output is omitted in
this case for brevity, as it is a deep model.