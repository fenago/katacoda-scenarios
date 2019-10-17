
Another popular pixel scaling method is to calculate the mean pixel value across the entire
training dataset, then subtract it from each image. This is called centering and has the effect
of centering the distribution of pixel values on zero: that is, the mean pixel value for centered
images will be zero. The ImageDataGenerator class refers to centering that uses the mean
calculated on the training dataset as feature-wise centering. It requires that the statistic is
calculated on the training dataset prior to scaling.
```
# create generator that centers pixel values
datagen = ImageDataGenerator(featurewise_center=True)
# calculate the mean on the training dataset
datagen.fit(trainX)
```

It is different to calculating of the mean pixel value for each image, which Keras refers to
as sample-wise centering and does not require any statistics to be calculated on the training
dataset.

```
# create generator that centers pixel values
datagen = ImageDataGenerator(samplewise_center=True)
# calculate the mean on the training dataset
datagen.fit(trainX)
```


We will demonstrate feature-wise centering in this section. Once the statistic is calculated
on the training dataset, we can confirm the value by accessing and printing it; for example:7.5. How to Center Images With ImageDataGenerator 68
```
# print the mean calculated on the training dataset.
print(datagen.mean)
```
