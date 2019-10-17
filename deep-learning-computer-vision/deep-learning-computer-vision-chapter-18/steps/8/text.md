The pre-trained model may be used as a standalone program to extract features from new
photographs. Specifically, the extracted features of a photograph may be a vector of numbers
that the model will use to describe the specific features in a photograph. These features can
then be used as input in the development of a new model. The last few layers of the VGG16
model are fully connected layers prior to the output layer. These layers will provide a complex18.6. Examples of Using Pre-Trained Models 199
set of features to describe a given input image and may provide useful input when training a
new model for image classification or related computer vision task.
The image can be loaded and prepared for the model, as we did before in the previous
example. We will load the model with the classifier output part of the model, but manually
remove the final output layer. This means that the second last fully connected layer with 4,096
nodes will be the new output layer.

```
# load model
model = VGG16()
# remove the output layer
model.layers.pop()
model = Model(inputs=model.inputs, outputs=model.layers[-1].output)
```

This vector of 4,096 numbers will be used to represent the complex features of a given input
image that can then be saved to file to be loaded later and used as input to train a new model.

```
We can save it as a pickle file.
# get extracted features
features = model.predict(image)
print(features.shape)
# save to file
dump(features, open('dog.pkl', 'wb'))
```


We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_18/05_pretrained_feature_extractor.py` to view file.


#### Run Code
Now, run the python code by running: `python 05_pretrained_feature_extractor.py`{{execute}}

Running the example loads the photograph, then prepares the model as a feature extraction
model. The features are extracted from the loaded photo and the shape of the feature vector is
printed, showing it has 4,096 numbers. This feature vector is then saved to a new file dog.pkl
in the current working directory.

```
(1, 4096)
```
