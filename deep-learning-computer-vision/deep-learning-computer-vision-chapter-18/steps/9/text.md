We can use some or all of the layers in a pre-trained model as a feature extraction component
of a new model directly. This can be achieved by loading the model, then simply adding new
layers. This may involve adding new convolutional and pooling layers to expand upon the
feature extraction capabilities of the model or adding new fully connected classifier type layers
to learn how to interpret the extracted features on a new dataset, or some combination. For
example, we can load the VGG16 models without the classifier part of the model by specifying
the include top argument to False, and specify the preferred shape of the images in our new
dataset as 300 x 300.

```
# load model without classifier layers
model = VGG16(include_top=False, input_shape=(300, 300, 3))
Listing 18.18: Example of loading the pre-trained model without the classifier output model.
We can then use the Keras functional API to add a new Flatten layer after the last pooling
layer in the VGG16 model, then define a new classifier model with a Dense fully connected
layer and an output layer that will predict the probability for 10 classes.
# add new classifier layers
flat1 = Flatten()(model.outputs)
class1 = Dense(1024, activation='relu')(flat1)
output = Dense(10, activation='softmax')(class1)
# define new model
model = Model(inputs=model.inputs, outputs=output)
```

An alternative approach to adding a Flatten layer would be to define the VGG16 model
with an average pooling layer, and then add fully connected layers. Perhaps try both approaches
on your application and see which results in the best performance. The weights of the VGG16
model and the weights for the new model will all be trained together on the new dataset.


We can run the centering code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_18/06_pretrained_model_with_new_output.py` to view file.

#### Run Code
Now, run the python code by running: `python 06_pretrained_model_with_new_output.py`{{execute}}

Running the example defines the new model ready for training and summarizes the model
architecture. We can see that we have flattened the output of the last pooling layer and added
our new fully connected layers.