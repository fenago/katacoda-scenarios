The Keras model can be used directly to predict the probability of a given face belonging
to one or more of more than eight thousand known celebrities; for example:

```
...
# perform prediction
yhat = model.predict(samples)
```

Once a prediction is made, the class integers can be mapped to the names of the celebrities,
and the top five names with the highest probability can be retrieved. This behavior is provided
by the decode predictions() function in the keras-vggface library.

```
...
# convert prediction into names
results = decode_predictions(yhat)
# display most likely results
for result in results[0]:
print('%s: %.3f%%' % (result[0], result[1]*100))
```

Before we can make a prediction with a face, the pixel values must be scaled in the same way
that data was prepared when the VGGFace model was fit. Specifically, the pixel values must
be centered on each channel using the mean from the training dataset. This can be achieved
using the preprocess input() function provided in the keras-vggface library and specifying
the version=2 so that the images are scaled using the mean values used to train the VGGFace2
models instead of the VGGFace1 models (the default).


```
...
# convert one face into samples
pixels = pixels.astype('float32')
samples = expand_dims(pixels, axis=0)
# prepare the face for the model, e.g. center pixels
samples = preprocess_input(samples, version=2)
```

We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_29/05_vggface_face_identification_stone.py` to view file.


#### Run Code
Now, run the python code by running: `python 05_vggface_face_identification_stone.py`{{execute}}

Running the example loads the photograph, extracts the single face that we know was
present, and then predicts the identity for the face. The top five highest probability names are
then displayed. We can see that the model correctly identifies the face as belonging to Sharon
Stone with a likelihood of 99.642%.

```
Sharon_Stone: 99.642%
Noelle_Reno: 0.085%
Elisabeth_R: 0.033%
Anita_Lipnicka: 0.026%
Tina_Maze: 0.019%
```
