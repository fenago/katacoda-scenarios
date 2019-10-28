In machine learning we are often interested in selecting the best hypothesis (h) given data (d).
In a classification problem, our hypothesis (h) may be the class to assign for a new data instance
(d). One of the easiest ways of selecting the most probable hypothesis given the data that we
have that we can use as our prior knowledge about the problem. Bayes’ Theorem provides a
way that we can calculate the probability of a hypothesis given our prior knowledge. Bayes’
Theorem is stated as:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-09/steps/3/1.JPG)

Where:
- P(h|d) is the probability of hypothesis h given the data d. This is called the posterior
probability.
- P(d|h) is the probability of data d given that the hypothesis h was true.
- P(h) is the probability of hypothesis h being true (regardless of the data). This is called
the prior probability of h.
- P(d) is the probability of the data (regardless of the hypothesis)
