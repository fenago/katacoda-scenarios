The InceptionV3 is the third iteration of the inception architecture, first developed for the
GoogLeNet model. This model was developed by researchers at Google and described in the 2015
paper titled Rethinking the Inception Architecture for Computer Vision. The model
expects color images to have the square shape 299 x 299. The model can be loaded as follows:

```
# example of loading the inception v3 model
from keras.applications.inception_v3 import InceptionV3
# load model
model = InceptionV3()
# summarize the model
model.summary()
```

We can run the centering code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_18/02_inception_model.py` to view file.


#### Run Code
Now, run the python code by running: `python 02_inception_model.py`{{execute}}

Running the example will load the model, downloading the weights if required, and then
summarize the model architecture to confirm it was loaded correctly.