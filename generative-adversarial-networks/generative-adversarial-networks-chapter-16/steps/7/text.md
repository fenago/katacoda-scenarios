Now that we have defined the GAN model, we need to train it. But, before we can train the
model, we require input data. The first step is to load and scale the MNIST dataset. The whole
dataset is loaded via a call to the load data() Keras function, then a subset of the images is
selected (about 5,000) that belongs to class 7, e.g. are a handwritten depiction of the number
seven. Then the pixel values must be scaled to the range [-1,1] to match the output of the
generator model. The load real samples() function below implements this, returning the
loaded and scaled subset of the MNIST training dataset ready for modeling.

```
# load images
def load_real_samples():
# load dataset
(trainX, trainy), (_, _) = load_data()
# select all of the examples for a given class
selected_ix = trainy == 7
X = trainX[selected_ix]
# expand to 3d, e.g. add channels
X = expand_dims(X, axis=-1)
# convert from ints to floats
X = X.astype('float32')
# scale from [0,255] to [-1,1]
X = (X - 127.5) / 127.5
return X
```
