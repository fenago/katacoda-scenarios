Gradient Descent is the process of minimizing a function by following the gradients of the cost
function. This involves knowing the form of the cost as well as the derivative so that from a
given point you know the gradient and can move in that direction, e.g. downhill towards the
minimum value. In machine learning we can use a technique that evaluates and update the
coefficients every iteration called stochastic gradient descent to minimize the error of a model
on our training data.

The way this optimization algorithm works is that each training instance is shown to the
model one at a time. The model makes a prediction for a training instance, the error is calculated
and the model is updated in order to reduce the error for the next prediction. This procedure
can be used to find the set of coefficients in a model that result in the smallest error for the
model on the training data. Each iteration, the coefficients called weights (w) in machine
learning language are updated using the equation:

```
w = w − alpha × delta
```

Where w is the coefficient or weight being optimized, alpha is a learning rate that you must
configure (e.g. 0.1) and delta is the error for the model on the training data attributed to the
weight