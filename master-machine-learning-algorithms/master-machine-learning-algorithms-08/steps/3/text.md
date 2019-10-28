Classification and Regression Trees or CART for short is a term introduced by Leo Breiman
to refer to Decision Tree algorithms that can be used for classification or regression predictive
modeling problems. Classically, this algorithm is referred to as decision trees, but on some
platforms like R they are referred to by the more modern term CART. The CART algorithm
provides a foundation for important algorithms like bagged decision trees, random forest and
boosted decision trees.

#### CART Model Representation
The representation for the CART model is a binary tree. This is your binary tree from algorithms
and data structures, nothing too fancy. Each node represents a single input variable (x) and
a split point on that variable (assuming the variable is numeric). The leaf nodes of the tree
contain an output variable (y) which is used to make a prediction. Given a dataset with two
inputs of height in centimeters and weight in kilograms the output of sex as male or female,
below is a crude example of a binary decision tree (completely fictitious for demonstration
purposes only).

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-08/steps/3/1.JPG)

The tree can be stored to file as a graph or a set of rules. For example, below is the above
decision tree as a set of rules.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-08/steps/3/2.JPG)