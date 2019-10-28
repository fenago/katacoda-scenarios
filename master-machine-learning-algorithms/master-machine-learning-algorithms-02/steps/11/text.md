Before we wrap up I want to show you a quick shortcut for calculating the coefficients. Simple
linear regression is the simplest form of regression and the most studied. There is a shortcut
that you can use to quickly estimate the values for B0 and B1. Really it is a shortcut for
calculating B1. The calculation of B1 can be re-written as:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-02/steps/11/1.JPG)

Where corr(x; y) is the correlation between x and y and stdev() is the calculation of the
standard deviation for a variable. Correlation (also known as Pearson’s correlation coefficient)
is a measure of how related two variables are in the range of -1 to 1. A value of 1 indicates that
the two variables are perfectly positively correlated, they both move in the same direction and
a value of -1 indicates that they are perfectly negatively correlated, when one moves the other
moves in the other direction.
Standard deviation is a measure of how much on average the data is spread out from the
mean. You can use the function PEARSON() in your spreadsheet to calculate the correlation of x
and y as 0.852 (highly correlated) and the function STDEV() to calculate the standard deviation
of x as 1.5811 and y as 1.4832. Plugging these values in we have:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-02/steps/11/2.JPG)
