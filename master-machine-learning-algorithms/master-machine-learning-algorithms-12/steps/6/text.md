- **Rescale Data:** KNN performs much better if all of the data has the same scale. Normalizing your data to the range between 0 and 1 is a good idea. It may also be a good idea to standardize your data if it has a Gaussian distribution.
- **Address Missing Data:** Missing data will mean that the distance between samples
cannot be calculated. These samples could be excluded or the missing values could be
imputed.
- **Lower Dimensionality:** KNN is suited for lower dimensional data. You can try it on
high dimensional data (hundreds or thousands of input variables) but be aware that it
may not perform as well as other techniques. KNN can benefit from feature selection that
reduces the dimensionality of the input feature space