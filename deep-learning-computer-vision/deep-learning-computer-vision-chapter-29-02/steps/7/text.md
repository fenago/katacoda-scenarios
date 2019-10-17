A VGGFace2 model can be used for face verification. This involves calculating a face embedding
for a new given face and comparing the embedding to the embedding for the single example
of the face known to the system. A face embedding is a vector that represents the features
extracted from the face. This can then be compared with the vectors generated for other faces.
For example, another vector that is close (by some measure) may be the same person, whereas
another vector that is far (by some measure) may be a different person.

Typical measures such as Euclidean distance and Cosine distance are calculated between two
embeddings and faces are said to match or verify if the distance is below a predefined threshold,
often tuned for a specific dataset or application. First, we can load the VGGFace model without
the classifier by setting the include top argument to False, specifying the shape of the output
via the input shape and setting pooling to avg so that the filter maps at the output end of
the model are reduced to a vector using global average pooling.

```
...
# create a vggface model
model = VGGFace(model='resnet50', include_top=False, input_shape=(224, 224, 3),
pooling='avg')
```

This model can then be used to make a prediction, which will return a face embedding for
one or more faces provided as input.

```
# perform prediction
yhat = model.predict(samples)
```
