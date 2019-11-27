
We must scale the pixel values from the range of unsigned integers in [0,255] to the normalized
range of [-1,1]. The generator model will generate images with pixel values in the range [-1,1] as
it will use the Tanh activation function, a best practice. It is also a good practice for the real
images to be scaled to the same range.

```
...
# convert from unsigned ints to floats
X = trainX.astype('float32')
# scale from [0,255] to [-1,1]
X = (X - 127.5) / 127.5
```

The load real samples() function below implements the loading and scaling of real CIFAR-
10 photographs.

```
# load and prepare cifar10 training images
def load_real_samples():
# load cifar10 dataset
(trainX, _), (_, _) = load_data()
# convert from unsigned ints to floats
X = trainX.astype('float32')
# scale from [0,255] to [-1,1]
X = (X - 127.5) / 127.5
return X
```
