In this section, we will use the VGGFace2 model to perform face recognition with photographs of
celebrities from Wikipedia. A VGGFace model can be created using the VGGFace() constructor
and specifying the type of model to create via the model argument.

```
...
model = VGGFace(model='...')
```

The keras-vggface library provides three pre-trained VGGModels, a VGGFace1 model via
model='vgg16' (the default), and two VGGFace2 models 'resnet50' and 'senet50'. The
example below creates a 'resnet50' VGGFace2 model and summarizes the shape of the inputs
and outputs.

```
# example of creating a face embedding
from keras_vggface.vggface import VGGFace
# create a vggface2 model
model = VGGFace(model='resnet50')
# summarize input and output shape
print('Inputs: %s' % model.inputs)
print('Outputs: %s' % model.outputs)
```


We can run the centering code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_29/04_vggface_model.py` to view file.


#### Run Code
Now, run the python code by running: `python 04_vggface_model.py`{{execute}}

The first time that a model is created, the library will download the model weights and
save them in the ./keras/models/vggface/ directory in your home directory. The size of the
weights for the resnet50 model is about 158 megabytes, so the download may take a few minutes
depending on the speed of your internet connection. Running the example prints the shape
of the input and output tensors of the model. We can see that the model expects input color
images of faces with the shape of 244 × 244 and the output will be a class prediction of 8,631
people.

```
Inputs: [<tf.Tensor 'input_1:0' shape=(?, 224, 224, 3) dtype=float32>]
Outputs: [<tf.Tensor 'classifier/Softmax:0' shape=(?, 8631) dtype=float32>]
```
