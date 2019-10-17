We can define a new function that, given a list of filenames for photos containing a face,
will extract one face from each photo via the extract face() function developed in a prior
section, pre-processing is required for inputs to the VGGFace2 model and can be achieved by
calling preprocess input(), then predict a face embedding for each. The get embeddings()
function below implements this, returning an array containing an embedding for one face for
each provided photograph filename.


```
# extract faces and calculate face embeddings for a list of photo files
def get_embeddings(filenames):
# extract faces
faces = [extract_face(f) for f in filenames]
# convert into an array of samples
samples = asarray(faces, 'float32')
# prepare the face for the model, e.g. center pixels
samples = preprocess_input(samples, version=2)
# create a vggface model
model = VGGFace(model='resnet50', include_top=False, input_shape=(224, 224, 3),
pooling='avg')
# perform prediction
yhat = model.predict(samples)
return yhat
```

We can take our photograph of Sharon Stone used previously (e.g. sharon stone1.jpg) as
our definition of the identity of Sharon Stone by calculating and storing the face embedding for
the face in that photograph. We can then calculate embeddings for faces in other photographs
of Sharon Stone and test whether we can effectively verify her identity. We can also use faces
from photographs of other people to confirm that they are not verified as Sharon Stone.
Verification can be performed by calculating the Cosine distance between the embedding
for the known identity and the embeddings of candidate faces. This can be achieved using
the cosine() SciPy function. The maximum distance between two embeddings is a score
of 1.0, whereas the minimum distance is 0.0. A common cut-off value used for face identity
is between 0.4 and 0.6, such as 0.5, although this should be tuned for an application. The
is match() function below implements this, calculating the distance between two embeddings
and interpreting the result.

```
# determine if a candidate face is a match for a known face
def is_match(known_embedding, candidate_embedding, thresh=0.5):
# calculate distance between embeddings
score = cosine(known_embedding, candidate_embedding)
if score <= thresh:
print('>face is a Match (%.3f <= %.3f)' % (score, thresh))
else:
print('>face is NOT a Match (%.3f > %.3f)' % (score, thresh))
```
