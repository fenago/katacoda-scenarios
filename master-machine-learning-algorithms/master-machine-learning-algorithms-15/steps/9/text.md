The predictions from the bootstrap models can be combined to produce more accurate predictions.
In this section we look at making predictions with each bootstrapped model, then finally aggregate
the submodel predictions into more accurate ensemble predictions.


##### Decision Stump Model 1
The split point for the first model is X1 ≤ 5:38660215. Using this split point we can separate
the training data into two groups:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-15/steps/9/1.JPG)

We can see that the LEFT group contains mostly instances for class 0 and the RIGHT group
contains mostly instances of class 1. Therefore, instances assigned to the two groups will be
classified:
- **LEFT**: class 0
- **RIGHT**: class 1

We can therefore calculate the prediction for each training instance.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-15/steps/9/2.JPG)

We can see that the model only got one training instance incorrect (the second last one).
This gives the model an accuracy of 90%. Not bad at all, but we can do better.