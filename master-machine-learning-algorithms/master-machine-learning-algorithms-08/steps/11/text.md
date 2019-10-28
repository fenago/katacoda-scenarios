
and X2. If we look at the graph of the data, we can see that we can probably draw a vertical
line to separate the classes. This would translate to a split point for X1 with a value around
0.5. A close fit would be the value for X1 in the last instance: X1 = 6:6422.
- IF X1 < 6:6422 THEN **LEFT**
- IF X1 ≥ 6:6422 THEN **RIGHT**
Let’s apply this rule to all instances, below we get the assigned group for each numbered
data instance:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-08/steps/11/1.JPG)

There are 5 instances in each group, this looks like a good split. Starting with the LEFT
group, we can calculate the proportion of training instances that have each class:
- Y = 0: 5/5 or 1.0
- Y = 1: 0/5 or 0.0

The `RIGHT` group has the opposite proportions.

- Y = 0: 0/5 or 0.0
- Y = 1: 5/5 or 1.0

We now have enough information to calculate the Gini index for this split:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-08/steps/11/2.JPG)

This is a split that results in a pure Gini index because the classes are perfectly separated.
The LEFT child node will classify instances as class 0 and the right as class 1. We can stop
there. You can see how this process could be repeated for each child node to build up a more
complicated tree for a more challenging dataset.

