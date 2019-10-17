
We can also confirm that the scaling procedure has had the desired effect by calculating the
mean of a batch of images returned from the batch iterator. We would expect the mean to be a
small value close to zero, but not zero because of the small number of images in the batch.

```
# get a batch
batchX, batchy = iterator.next()
# mean pixel value in the batch
print(batchX.shape, batchX.mean())
```

A better check would be to set the batch size to the size of the training dataset (e.g. 60,000
samples), retrieve one batch, then calculate the mean. It should be a very small value close to
zero.

```
# try to flow the entire training dataset
iterator = datagen.flow(trainX, trainy, batch_size=len(trainX), shuffle=False)
# get a batch
batchX, batchy = iterator.next()
# mean pixel value in the batch
print(batchX.shape, batchX.mean())
```

