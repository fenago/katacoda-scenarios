We can make it more interesting by plotting the original face and the prediction. First, we
need to load the face dataset, specifically the faces in the test dataset. We could also load the
original photos to make it even more interesting.

```
# load faces
data = load(
'5-celebrity-faces-dataset.npz
')
testX_faces = data[
'arr_2
']
```

The rest of the example is the same up until we fit the model. First, we need to select a
random example from the test set, then get the embedding, face pixels, expected class prediction,
and the corresponding name for the class.

We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_30/07_random_face_identity_classification.py` to view file.


#### Run Code
Now, run the python code by running: `python 07_random_face_identity_classification.py`{{execute}}

Running the example first confirms that the number of samples in the train and test datasets
is as we expect Next, the model is evaluated on the train and test dataset, showing perfect
classification accuracy. This is not surprising given the size of the dataset and the power of the
face detection and face recognition models used.

A different random example from the test dataset will be selected each time the code is
run. Try running it a few times. In this case, a photo of Jerry Seinfeld is selected and correctly
predicted.

```
Predicted: jerry_seinfeld (88.476)
Expected: jerry_seinfeld
```
