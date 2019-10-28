We can make predictions using Bayes Theorem, introduced and explained in a previous chapter.
We don’t need a probability to predict the most likely class for a new data instance. We only
need the numerator and the class that gives the largest response is the predicted response.

`MAP(h) = max(P(d|h) × P(h))`

Let’s take the first record from our dataset and use our learned model to predict which class
we think it belongs. Instance: X1 = 3:393533211, X2 = 2.331273381, Y = 0. We can plug the
probabilities for our model in for both classes and calculate the response. Starting with the
response for the output class 0. We multiply the conditional probabilities together and multiply
it by the probability of any instance belonging to the class.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-11/steps/8/1.JPG)

We can see that 0.050324277 is greater than 0.000115577, therefore we predict the class as 0
for this instance, which is correct. Repeating this process for all instances in the dataset we get
the following outcomes for class 0 and class 1. By selecting the class with the highest output we
make accurate predictions for all instances in the training dataset.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-11/steps/8/2.JPG)

The prediction accuracy is 100%, as was expected given the clear separation of the classes.
