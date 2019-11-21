The first step is to load and prepare the Fashion-MNIST dataset. We only require the images
in the training dataset. The images are black and white, therefore we must add an additional
channel dimension to transform them to be three dimensional, as expected by the convolutional
layers of our models. Finally, the pixel values must be scaled to the range [-1,1] to match the
output of the generator model. The load real samples() function below implements this,
returning the loaded and scaled Fashion-MNIST training dataset ready for modeling.

```
# load images
def load_real_samples():
# load dataset
(trainX, trainy), (_, _) = load_data()
# expand to 3d, e.g. add channels
X = expand_dims(trainX, axis=-1)
# convert from ints to floats
X = X.astype('float32')
# scale from [0,255] to [-1,1]
X = (X - 127.5) / 127.5
print(X.shape, trainy.shape)
return [X, trainy]
```
