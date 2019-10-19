The next step is to create a face embedding. A face embedding is a vector that represents the
features extracted from the face. This can then be compared with the vectors generated for
other faces. For example, another vector that is close (by some measure) may be the same
person, whereas another vector that is far (by some measure) may be a different person. The
classifier model that we want to develop will take a face embedding as input and predict the
identity of the face. The FaceNet model will generate this embedding for a given image of a
face.
The FaceNet model can be used as part of the classifier itself, or we can use the FaceNet
model to pre-process a face to create a face embedding that can be stored and used as input to
our classifier model. This latter approach is preferred as the FaceNet model is both large and
slow to create a face embedding. We can, therefore, pre-compute the face embeddings for all
faces in the train and test (formally val) sets in our 5 Celebrity Faces Dataset. First, we can
load our detected faces dataset using the load() NumPy function

We can run the code now. Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `deep-learning-python/chapter_30/05_predict_face_embeddings.py` to view file.


#### Run Code
Now, run the python code by running: `python 05_predict_face_embeddings.py`{{execute}}


Running the example reports progress along the way. We can see that the face dataset was
loaded correctly and so was the model. The train dataset was then transformed into 93 face embeddings, each comprised of a 128 element vector. 
The 25 examples in the test dataset were also
suitably converted to face embeddings. The resulting datasets were then saved to a compressed
NumPy array that is about 50 kilobytes with the name 5-celebrity-faces-embeddings.npz
in the current working directory.

```
Loaded: (93, 160, 160, 3) (93,) (25, 160, 160, 3) (25,)
Loaded Model
(93, 128)
(25, 128)
```

We are now ready to develop our face classifier system.
