Random Forests are an improvement over bagged decision trees. A problem with decision trees
like CART is that they are greedy. They choose which variable to split on using a greedy
algorithm that minimizes error. As such, even with Bagging, the decision trees can have a lot
of structural similarities and in turn result in high correlation in their predictions. Combining
predictions from multiple models in ensembles works better if the predictions from the submodels
are uncorrelated or at best weakly correlated.

Random forest changes the algorithm for the way that the sub-trees are learned so that
the resulting predictions from all of the subtrees have less correlation. It is a simple tweak.
In CART, when selecting a split point, the learning algorithm is allowed to look through all
variables and all variable values in order to select the most optimal split-point. The random
forest algorithm changes this procedure so that the learning algorithm is limited to a random
sample of features of which to search. The number of features that can be searched at each split
point (m) must be specified as a parameter to the algorithm. You can try different values and
tune it using cross-validation.

- For **classification** a good default is: ![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-15/steps/5/1.JPG)
- For **regression** a good default is: ![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-15/steps/5/2.JPG)

Where m is the number of randomly selected features that can be searched at a split point
and p is the number of input variables. For example, if a dataset had 25 input variables for a
classification problem, then:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-15/steps/5/3.JPG)
