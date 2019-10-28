How good was this split? We can evaluate the mixture of the classes in each of the LEFT
and RIGHT nodes as a single cost of choosing this split point for our root node. The LEFT
group only has one member, where as the RIGHT group has 9 members. Starting with the
LEFT group, we can calculate the proportion of training instances that have each class:
- Y = 0: 1/1 or 1.0
- Y = 1: 0/1 or 0.0
The RIGHT group is more interesting as it is comprised of a mix of classes (we are probably
going to get a high Gini index).
- Y = 0: 4/9 or 0.4444
- Y = 1: 5/9 or 0.5555

We now have enough information to calculate the Gini index for this split:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-08/steps/10/1.JPG)
