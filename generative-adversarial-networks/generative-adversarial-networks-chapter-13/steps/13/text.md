It may be useful to calculate the FID score between two collections of real images. The
Keras library provides a number of computer vision datasets, including the CIFAR-10 dataset
(described in Section 8.2). These are color photos with the small size of 32 × 32 pixels and is
split into train and test elements and can be loaded as follows:

```
...
# load cifar-10 images
(images, _), (_, _) = cifar10.load_data()
```

The training dataset has 50,000 images, whereas the test dataset has only 10,000 images. It
may be interesting to calculate the FID score between these two datasets to get an idea of how
representative the test dataset is of the training dataset. Scaling and scoring 50K images takes
a long time, therefore, we can reduce the training set to a 10K random sample as follows:

```
...
shuffle(images1)
images1 = images1[:10000]
```