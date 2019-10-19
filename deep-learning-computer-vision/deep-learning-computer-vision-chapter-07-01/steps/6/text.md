How to Normalize Images With ImageDataGenerator
The ImageDataGenerator class can be used to rescale pixel values from the range of 0-255 to the
range 0-1 preferred for neural network models. Scaling data to the range of 0-1 is traditionally
referred to as normalization. This can be achieved by setting the rescale argument to a ratio by
which each pixel can be multiplied to achieve the desired range. In this case, the ratio is 255 1 or
about 0.0039.

```
...
# create generator (1.0/255.0 = 0.003921568627451)
datagen = ImageDataGenerator(rescale=1.0/255.0)
```

The ImageDataGenerator does not need to be fit in this case because there are no global
statistics line mean and standard deviation that need to be calculated. Next, iterators can be
created using the generator for both the train and test datasets. We will use a batch size of 64. This means that each of the train and test datasets of images are divided into groups of 64
images that will then be scaled when returned from the iterator. We can see how many batches
there will be in one epoch, e.g. one pass through the training dataset, by printing the length of
each iterator.

```
# prepare an iterators to scale images
train_iterator = datagen.flow(trainX, trainY, batch_size=64)
test_iterator = datagen.flow(testX, testY, batch_size=64)
print('Batches train=%d, test=%d' % (len(train_iterator), len(test_iterator)))
```

We can then confirm that the pixel normalization has been performed as expected by
retrieving the first batch of scaled images and inspecting the min and max pixel values.

```
# confirm the scaling works
batchX, batchy = train_iterator.next()
print('Batch shape=%s, min=%.3f, max=%.3f' % (batchX.shape, batchX.min(), batchX.max()))
```
