The split point used by the third model is X2 ≤ 0.925340325. Using this split point, we can
again sort the training dataset into two groups.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-15/steps/11/1.JPG)

In this model the RIGHT group will classify instances as class 0 and the LEFT group as
class 1. Using this simple model, we can again make predictions for each training instance.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-15/steps/11/2.JPG)

This model has slightly worse accuracy of 70%. Importantly it correctly predicts both the
second last instance and the 5th instance, clearing up any ambiguity if the previous two models
were combined.