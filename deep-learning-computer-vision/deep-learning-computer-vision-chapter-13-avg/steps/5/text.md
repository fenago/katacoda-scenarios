
Again, given the horizontal symmetry of the feature map provided for pooling, we would
expect the pooled feature map to look as follows:

```
[0.0, 3.0, 0.0]
[0.0, 3.0, 0.0]
[0.0, 3.0, 0.0]
```

It just so happens that the chosen line detector image and feature map produce the same
output when downsampled with average pooling and maximum pooling. The maximum pooling
operation can be added to the worked example by adding the MaxPooling2D layer provided by
the Keras API.


```
# create model
model = Sequential()
model.add(Conv2D(1, (3,3), activation=relu, input_shape=(8, 8, 1)))
model.add(MaxPooling2D())
```
Above Example shows how to define a model with one filter and max pooling.
