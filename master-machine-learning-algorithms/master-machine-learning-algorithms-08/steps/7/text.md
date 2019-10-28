We calculate the Gini index for a child node as follows:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-08/steps/7/1.JPG)

Where p1 is the proportion of instances in the node with class 1 and p2 is the proportion
of instances in the node for class 2. We will always have two groups, a LEFT and RIGHT
group because we are using a binary tree. And we know from our dataset that we only have
two classes.

The proportion of data instances of a class is easy to calculate. If a LEFT group has 3
instances with class 0 and 4 instances with class 1, then the proportion of data instances with18.2. Learning a CART Model 79
class 0 would be 3/7 or 0.428571429. To get a feeling for Gini index scores for child nodes, take a
look at the table below. It provides 7 different scenarios for mixes of 0 and 1 classes in a single
group.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-08/steps/7/2.JPG)


