In this section we will work through a few updates to the coefficients to demonstrate the SVM
learning algorithm. We will use a very large lambda value: lambda = 0.45. This is unusually
large and will force a lot of change on each update. Normally lambda values are very small.

#### Learning Iteration #1
We will start by setting the coefficients to 0.0.

```
B1 = 0.0
B2 = 0.0
```

We also need to keep track of which iteration we are on: t = 1. We will train the model
using the order of the training patterns. Ideally, the order of the patterns would be randomized
to avoid the learning algorithm getting stuck. The first training pattern we will use to update27.3. Learn an SVM Model from Training Data 123
the coefficients is: Instance: X1 = 2.327868056, X2 = 2.458016525, Y = −1. We can now
calculate the output value for this iteration.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-14/steps/9/1.JPG)

Easy enough. The output is less than 1.0, therefore we will use the more complex update
procedure that assumes the training pattern is a support vector:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-14/steps/9/2.JPG)
