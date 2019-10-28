This section lists some suggestions you may consider when preparing your data for use with
LDA.

- **Classification Problems.** This might go without saying, but LDA is intended for
classification problems where the output variable is categorical. LDA supports both binary
and multiclass classification.
- **Gaussian Distribution.** The standard implementation of the model assumes a Gaussian
distribution of the input variables. Consider reviewing the univariate distributions of each
attribute and using transforms to make them more Gaussian-looking (e.g. log and root
for exponential distributions and Box-Cox for skewed distributions).
- **Remove Outliers.** Consider removing outliers from your data. These can skew the basic
statistics used to separate classes in LDA such as the mean and the standard deviation.
- **Same Variance.** LDA assumes that each input variable has the same variance. It’s
almost always a good idea to standardize your data before using LDA so that it has a
mean of 0 and a standard deviation of 1.