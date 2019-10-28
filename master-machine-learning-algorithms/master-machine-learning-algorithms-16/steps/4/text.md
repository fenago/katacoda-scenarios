AdaBoost is best used to boost the performance of decision trees on binary classification
problems. AdaBoost was originally called AdaBoost.M1 by the developers of the technique.
More recently it may be referred to as discrete AdaBoost because it is used for classification
rather than regression. AdaBoost can be used to boost the performance of any machine learning
algorithm. It is best used with weak learners.

These are models that achieve accuracy just above random chance on a classification problem.
The most suited and therefore most common algorithm used with AdaBoost are decision trees
with one level. Because these trees are so short and only contain one decision for classification,
they are often called decision stumps. Each instance in the training dataset is weighted. The
initial weight is set to:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-16/steps/4/1.JPG)

Where xi is the i’th training instance and n is the number of training instances.