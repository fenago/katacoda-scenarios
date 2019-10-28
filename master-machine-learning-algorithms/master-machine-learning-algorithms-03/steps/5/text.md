
The coefficients used in simple linear regression can be found using stochastic gradient descent.
Stochastic gradient descent is not used to calculate the coefficients for linear regression in
practice unless the dataset prevents traditional Ordinary Least Squares being used (e.g. a
very large dataset). Nevertheless, linear regression does provide a useful exercise for practicing
stochastic gradient descent which is an important algorithm used for minimizing cost functions
by machine learning algorithms. As stated in the previous chapter, our linear regression model
is defined as follows:

```
y = B0 + B1 × x
```
