There are a number of projects that provide tools to train FaceNet-based models and make
use of pre-trained models. Perhaps the most prominent is called OpenFace1 that provides
FaceNet models built and trained using the PyTorch deep learning framework. There is a port
of OpenFace to Keras, called Keras OpenFace2, but at the time of writing, the models appear
to require Python 2, which is quite limiting.

Another prominent project is called FaceNet by David Sandberg3 that provides FaceNet
models built and trained using TensorFlow. The project looks mature, although at the time of
writing does not provide a library-based installation nor clean API. Usefully, David’s project
provides a number of high-performing pre-trained FaceNet models and there are a number of
projects that port or convert these models for use in Keras. A notable example is Keras FaceNet
by Hiroki Taniai4. His project provides a script for converting the Inception ResNet v1 model
from TensorFlow to Keras. He also provides a pre-trained Keras model ready for use. We will
use the pre-trained Keras FaceNet model provided by Hiroki Taniai in this tutorial. It was
trained on MS-Celeb-1M dataset and expects input images to be color, to have their pixel values
whitened (standardized across all three channels), and to have a square shape of 160 × 160
pixels.

`wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1NcNe2q8pJOCBSmmwAlXikdquFUiqkAAd' -O facenet_keras.h5`{{execute}}

Model file has been downloaded and placed it in your current working directory with the filename
facenet_keras.h5. We can load the model directly in Keras using the load model() function;
for example:

```
# example of loading the keras facenet model
from keras.models import load_model
# load the model
model = load_model(facenet_keras.h5)
# summarize input and output shape
print(model.inputs)
print(model.outputs)
```

We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_30/01_facenet_model.py` to view file.

#### Run Code
Now, run the python code by running: `python 01_facenet_model.py`{{execute}}

Running the example loads the model and prints the shape of the input and output tensors.
We can see that the model indeed expects square color images as input with the shape 160×160,
and will output a face embedding as a 128 element vector.