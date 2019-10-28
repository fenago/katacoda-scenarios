Given the representation is a linear equation, making predictions is as simple as solving the
equation for a specific set of inputs. Let’s make this concrete with an example. Imagine we
are predicting weight (y) from height (x). Our linear regression model representation for this
problem would be:

```
y = B0 + B1 x X1
weight = B0 + B1 x height
```

Where B0 is the bias coefficient and B1 is the coefficient for the height column. We use a
learning technique to find a good set of coefficient values. Once found, we can plug in different
height values to predict the weight. For example, let’s use B0 = 0.1 and B1 = 0.5. Let’s plug
them in and calculate the weight (in kilograms) for a person with the height of 182 centimeters.

```
weight = 0.1 + 0.5 × 182
weight = 91.1
```

You can see that the above equation could be plotted as a line in two-dimensions. The B0
is our starting point regardless of what height we have. We can run through a bunch of heights
from 100 to 250 centimeters and plug them to the equation and get weight values, creating our
line.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-01/steps/5/1.png)

Now that we know how to make predictions given a learned linear regression model, let’s
look at some rules of thumb for preparing our data to make the most of this type of model
