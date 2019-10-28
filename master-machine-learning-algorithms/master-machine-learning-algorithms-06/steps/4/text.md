The representation of LDA is pretty straight forward. It consists of statistical properties of your
data, calculated for each class. For a single input variable (x) this is the mean and the variance
of the variable for each class.

For multiple variables, the same properties calculated over the multivariate Gaussian, namely
the means and the covariance matrix (this is a multi-dimensional generalization of variance).
These statistical properties are estimated from your data and plug into the LDA equation to
make predictions. These are the model values that you would save to file for your model. Let’s
look at how these parameters are estimated.
