When we have a single input attribute (x) and we want to use linear regression, this is called
simple linear regression. If we had multiple input attributes (e.g. X1, X2, X3, etc.) This would
be called multiple linear regression. The procedure for linear regression is different and simpler
than that for multiple linear regression, so it is a good place to start. In this section we are
going to create a simple linear regression model from our training data, then make predictions
for our training data to get an idea of how well the model learned the relationship in the data.
With simple linear regression we want to model our data as follows:

```
y = B0 + B1 x X
```

This is a line where y is the output variable we want to predict, x is the input variable
we know and B0 and B1 are coefficients that we need to estimate that move the line around.
Technically, B0 is called the intercept because it determines where the line intercepts the y-axis.
In machine learning we can call this the bias, because it is added to offset all predictions that
we make. The B1 term is called the slope because it defines the slope of the line or how x
translates into a y value before we add our bias.
