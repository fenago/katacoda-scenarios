The logistic regression model takes real-valued inputs and makes a prediction as to the probability
of the input belonging to the default class (class 0). If the probability is greater than 0.5 we can
take the output as a prediction for the default class (class 0), otherwise the prediction is for
the other class (class 1). For this dataset, the logistic regression has three coefficients just like
linear regression, for example:

`output = B0 + B1 × X1 + B2 × X2`

The job of the learning algorithm will be to discover the best values for the coefficients (B0,
B1 and B2) based on the training data. Unlike linear regression, the output is transformed into
a probability using the logistic function:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-05/steps/4/1.JPG)


#### Logistic Regression by Stochastic Gradient Descent
We can estimate the values of the coefficients using stochastic gradient descent. We can apply
stochastic gradient descent to the problem of finding the coefficients for the logistic regression
model.