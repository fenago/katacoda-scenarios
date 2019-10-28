It is easy to visualize these scenarios for one group, but the concepts translate to summing
the proportions across the LEFT and RIGHT groups. You can see when the group has a 50-50
mix in the first row, that Gini is 0.5. This is the worst possible split. You can also see a case
where the group only has data instances with class 0 on the last row and a Gini index of 0. This
is an example of a perfect split.

The calculation of the Gini index for a chosen split point involves calculating the Gini index
for each child node and weighting the scores by the number of instances in the parent node, as
follows:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-08/steps/8/1.JPG)

Our goal in selecting a split point is to evaluate the Gini index of all possible split points and
greedily select the split point with the lowest cost. Let’s make this more concrete by calculating
the cost of selecting different data points as our split point.