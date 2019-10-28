LDA makes predictions by estimating the probability that a new set of inputs belongs to each
class. The class that gets the highest probability is the output class and a prediction is made.
The model uses Bayes Theorem to estimate the probabilities. Briefly Bayes Theorem can be15.5. Preparing Data For LDA 64
used to estimate the probability of the output class (k) given the input (x) using the probability
of each class and the probability of the data belonging to each class:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-06/steps/6/1.JPG)

A Gaussian distribution function can be used to estimate P (xjk). Plugging the Gaussian
into the above equation and simplifying we end up with the equation below. It is no longer a
probability as we discard some terms. Instead it is called a discriminate function for class k. It
is calculated for each class k and the class that has the largest discriminant value will make the
output classification (Y = k):

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-06/steps/6/2.JPG)
