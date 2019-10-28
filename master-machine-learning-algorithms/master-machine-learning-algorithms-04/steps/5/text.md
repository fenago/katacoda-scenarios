Logistic regression uses an equation as the representation, very much like linear regression.
Input values (x) are combined linearly using weights or coefficient values to predict an output
value (y). A key difference from linear regression is that the output value being modeled is a
binary values (0 or 1) rather than a numeric value.

Below is an example logistic regression equation:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-04/steps/5/1.JPG)

Where y is the predicted output, B0 is the bias or intercept term and B1 is the coefficient
for the single input value (x). Each column in your input data has an associated B coefficient
(a constant real value) that must be learned from your training data. The actual representation
of the model that you would store in memory or in a file are the coefficients in the equation
(the beta value or B’s)