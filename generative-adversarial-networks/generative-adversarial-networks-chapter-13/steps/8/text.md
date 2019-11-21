Now that we know how to calculate the FID score and to implement it in NumPy, we can
develop an implementation in Keras. This involves the preparation of the image data and using
a pre-trained Inception v3 model to calculate the activations or feature vectors for each image.
First, we can load the Inception v3 model in Keras directly.

```
...
# load inception v3 model
model = InceptionV3()
```

This will prepare a version of the inception model for classifying images as one of 1,000
known classes. We can remove the output (the top) of the model via the include top=False
argument. Painfully, this also removes the global average pooling layer that we require, but
we can add it back via specifying the pooling=‘avg’ argument. When the output layer of the
model is removed, we must specify the shape of the input images, which is 299 × 299 × 3 pixels,
e.g. the input shape=(299,299,3) argument. Therefore, the inception model can be loaded
as follows:

```
...
# prepare the inception v3 model
model = InceptionV3(include_top=False, pooling='avg', input_shape=(299,299,3))
```
