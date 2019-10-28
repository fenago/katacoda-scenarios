We can make predictions using Bayes Theorem, defined and explained in the previous chapter.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-09/steps/9/1.JPG)

In fact, we don’t need a probability to predict the most likely class for a new data instance.
We only need the numerator and the class that gives the largest response, which will be the
predicted output.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-09/steps/9/2.JPG)

Let’s take the first record from our dataset and use our learned model to predict which class
we think it belongs. First instance: weather = sunny; car = working.
We plug the probabilities for our model in for both classes and calculate the response.
Starting with the response for the output go-out. We multiply the conditional probabilities
together and multiply it by the probability of any instance belonging to the class.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-09/steps/9/3.JPG)

We can see that 0.32 is greater than 0.04, therefore we predict go-out for this instance,
which is correct. We can repeat this operation for the entire dataset, as follows:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-09/steps/9/4.JPG)


If we tally up the predictions compared to the actual class values, we get an accuracy of
80%, which is excellent given that there are conflicting examples in the dataset.