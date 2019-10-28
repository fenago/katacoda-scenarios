Learning a naive Bayes model from your training data is fast. Training is fast because only the
probability of each class and the probability of each class given different input (x) values need
to be calculated. No coefficients need to be fitted by optimization procedures.

#### Calculating Class Probabilities
The class probabilities are simply the frequency of instances that belong to each class divided
by the total number of instances. For example in a binary classification the probability of an
instance belonging to class 1 would be calculated as:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-09/steps/5/1.JPG)

In the simplest case each class would have the probability of 0.5 or 50% for a binary
classification problem with the same number of instances in each class.

#### Calculating Conditional Probabilities
The conditional probabilities are the frequency of each attribute value for a given class value
divided by the frequency of instances with that class value. For example, if a weather attribute
had the values sunny and rainy and the class attribute had the class values go-out and
stay-home, then the conditional probabilities of each weather value for each class value could
be calculated as:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-09/steps/5/2.JPG)
