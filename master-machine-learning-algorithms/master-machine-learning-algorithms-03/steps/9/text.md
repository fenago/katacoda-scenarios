You can see that our final coefficients have the values B0 = 0.230897491 and B1 = 0.79043861.
Let’s plug them into our simple linear Regression model and make a prediction for each point
in our training dataset.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-03/steps/9/1.JPG)

We can plot our dataset again with these predictions overlaid (x vs y and x vs prediction).
Drawing a line through the 5 predictions gives us an idea of how well the model fits the training
data.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-03/steps/9/2.JPG)


We can calculate the RMSE for these predictions as we did in the previous chapter. The
result comes out to be RMSE = 0.720626401. This is very close to the RMSE achieved in
the previous section, but not the same. This is because RMSE is an optimization procedure
and must discover a good solution which may not be the same set of coefficients calculated
analytically. Gradient descent should only be used when analytical methods cannot be used,
such as having very large amounts of data.