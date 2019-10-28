LDA makes some assumptions about your data:
- The input variables have a Gaussian (bell curve) distribution.
- The variance (average squared difference from the mean) calculated for each input variables
by class grouping is the same.
- That the mix of classes in your training set is representative of the problem.

Below is a contrived simple two-dimensional dataset containing the input variable X and the
output class variable Y . All values for X were drawn from a Gaussian distribution and the class
variable Y has the value 0 or 1. The instances in the two classes were separated to make the
prediction problem simpler. All instances in class 0 were drawn from a Gaussian distribution
with a mean of 5 and a standard deviation of 1. All instances in class 1 were drawn from a
Gaussian distribution with a mean of 20 and a standard deviation of 1.

The classes do not interact and should be separable with a linear model like LDA. It is also
handy to know the actual statistical properties of the data because we can generate more test
instances later to see how well LDA has learned the model. Below is the complete dataset.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-06/steps/11/1.JPG)

Below is a plot of the dataset, showing the separation of the two classes.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-06/steps/11/2.JPG)
