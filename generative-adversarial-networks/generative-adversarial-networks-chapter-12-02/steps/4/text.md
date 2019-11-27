Now that we know how to calculate the inception score and to implement it in Python, we can
develop an implementation in Keras. This involves using the real Inception v3 model to classify
images and to average the calculation of the score across multiple splits of a collection of images.
First, we can load the Inception v3 model in Keras directly.

```
...
# load inception v3 model
model = InceptionV3()
```

The model expects images to be color and to have the shape 299 × 299 pixels. Additionally,
the pixel values must be scaled in the same way as the training data images, before they can be
classified. This can be achieved by converting the pixel values from integers to floating point
values and then calling the preprocess input() function for the images.

```
...
# convert from uint8 to float32
processed = images.astype('float32')
# pre-process raw images for inception v3 model
processed = preprocess_input(processed)
```
