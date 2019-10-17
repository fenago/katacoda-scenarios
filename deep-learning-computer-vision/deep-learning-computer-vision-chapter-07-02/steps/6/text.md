Standardization is a data scaling technique that assumes that the distribution of the data is
Gaussian and shifts the distribution of the data to have a mean of zero and a standard deviation
of one. Data with this distribution is referred to as a standard Gaussian. It can be beneficial
when training neural networks as the dataset sums to zero and the inputs are small values in
the rough range of about -3.0 to 3.0 (e.g. 99.7 of the values will fall within three standard
deviations of the mean). Standardization of images is achieved by subtracting the mean pixel
value and dividing the result by the standard deviation of the pixel values. The mean and
standard deviation statistics can be calculated on the training dataset, and as discussed in the
previous section, Keras refers to this as feature-wise.

```
# feature-wise generator
datagen = ImageDataGenerator(featurewise_center=True, featurewise_std_normalization=True)
# calculate mean and standard deviation on the training dataset
datagen.fit(trainX)
```

The statistics can also be calculated then used to standardize each image separately, and
Keras refers to this as sample-wise standardization.

```
# sample-wise standardization
datagen = ImageDataGenerator(samplewise_center=True, samplewise_std_normalization=True)7.6. How to Standardize Images With ImageDataGenerator 70
# calculate mean and standard deviation on the training dataset
datagen.fit(trainX)
```

We will demonstrate the feature-wise approach to image standardization in this section. The
effect will be batches of images with an approximate mean of zero and a standard deviation
of one. As with the previous section, we can confirm this with some simple experiments. 
