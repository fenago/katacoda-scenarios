You can see that we are interested in calculating the posterior probability of P(hjd) from
the prior probability p(h) with P(d) and P(djh). After calculating the posterior probability for
a number of different hypotheses, you can select the hypothesis with the highest probability.
This is the maximum probable hypothesis and may formally be called the maximum a posteriori
(MAP) hypothesis. This can be written as:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-09/steps/4/1.JPG)

The P(d) is a normalizing term which allows us to calculate the probability. We can drop
it when we are interested in the most probable hypothesis as it is constant and only used to
normalize. Back to classification, if we have an even number of instances in each class in our
training data, then the probability of each class (e.g. P(h)) will be the same value for each class
(e.g. 0.5 for a 50-50 split). Again, this would be a constant term in our equation and we could
drop it so that we end up with:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-09/steps/4/2.JPG)

This is a useful exercise, because when reading up further on Naive Bayes you may see all of
these forms of the theorem.