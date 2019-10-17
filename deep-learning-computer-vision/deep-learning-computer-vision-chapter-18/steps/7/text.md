A pre-trained model can be used directly to classify new photographs as one of the 1,000 known
classes in the image classification task in the ILSVRC. We will use the VGG16 model to classify
new images. First, the photograph needs to loaded and reshaped to a 224x224 square, expected
by the model, and the pixel values scaled in the way expected by the model. The model operates
on an array of samples, therefore the dimensions of a loaded image need to be expanded by 1,
for one image with 224 x 224 pixels and three channels.

```
# load an image from file
image = load_img('dog.jpg', target_size=(224, 224))
# convert the image pixels to a numpy array
image = img_to_array(image)
# reshape data for the model
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
# prepare the image for the VGG model
image = preprocess_input(image)
```

Next, the model can be loaded and a prediction made. This means that a predicted
probability of the photo belonging to each of the 1,000 classes is made. In this example, we are
only concerned with the most likely class, so we can decode the predictions and retrieve the
label or name of the class with the highest probability.

```
# predict the probability across all output classes
yhat = model.predict(image)
# convert the probabilities to class labels
label = decode_predictions(yhat)
# retrieve the most likely result, e.g. highest probability
label = label[0][0]
```

We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_18/04_pretrained_classifier.py` to view file.

#### Run Code
Now, run the python code by running: `python 04_pretrained_classifier.py`{{execute}}

Running the example predicts more than just dog; it also predicts the specific breed of
Doberman with a probability of 33.59%, which may, in fact, be correct.

```
Doberman (33.59%)
```
