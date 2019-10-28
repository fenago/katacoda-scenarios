The second model uses the split point X1 ≤ 4:090032824. We can separate the training data
into two groups:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-15/steps/10/1.JPG)

As above, the LEFT group will classify instances as class 0 and the RIGHT as class 1. Using
this model, we can make predictions for all instances in the training dataset:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-15/steps/10/2.JPG)

Again, like the first model, we can see the accuracy is 90% with only one instance misclassified.
This time the 5th instance. Combining just these two models results in some ambiguous
predictions where the models conflict in their predictions. Adding a third model will clear things
up.