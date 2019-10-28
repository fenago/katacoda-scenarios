Using the Gaussian PDF we can estimate the likelihood of range of values.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-11/steps/5/1.JPG)

You can see that the mean has the highest probability of nearly 0.4 (40%). You can also see
values that are far away from the mean like -5 and +5 (5 standard deviations from the mean)
have a very low probability. Below is a plot of the probabilities values.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-11/steps/5/2.JPG)

This function is really useful for Naive Bayes. We can assume that the input variables are
each drawn from a Gaussian distribution. By calculating the mean and standard deviation
of each input variable from the training data, we can use the Gaussian PDF to estimate the
likelihood of each value for each class. We will see how this is used to calculate conditional
probabilities in the next section.