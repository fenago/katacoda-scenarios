Maximum pooling, or max pooling, is a pooling operation that calculates the maximum, or
largest, value in each patch of each feature map. The results are downsampled or pooled feature
maps that highlight the most present feature in the patch, not the average presence of the
features, as in the case of average pooling. This has been found to work better in practice than
average pooling for computer vision tasks like image classification.

In a nutshell, the reason is that features tend to encode the spatial presence of some
pattern or concept over the different tiles of the feature map (hence, the term feature
map), and it’s more informative to look at the maximal presence of different features
than at their average presence.

We can make the max pooling operation concrete by again applying it to the output feature
map of the line detector convolutional operation and manually calculate the first row of the
pooled feature map. The first line of pooling input (first two rows and six columns) of the
output feature map were as follows:

```
[0.0, 0.0, 3.0, 3.0, 0.0, 0.0]
[0.0, 0.0, 3.0, 3.0, 0.0, 0.0]
```
