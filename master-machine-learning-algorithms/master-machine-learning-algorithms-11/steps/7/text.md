The conditional probabilities are the probabilities of each input value given each class value.
The conditional probabilities that need to be collected from the training data are as follows:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-11/steps/7/1.JPG)

The X1 and X2 input variables are real values. As such we will model them as having being
drawn from a Gaussian distribution. This will allow us to estimate the probability of a given
value using the Gaussian PDF described above. The Gaussian PDF requires two parameters in
addition to the value for which the probability is being estimated: the mean and the standard
deviation. Therefore we must estimate the mean and the standard deviation for each group of
conditional probabilities that we require. We can estimate these directly from the dataset. The
results are summarized below.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-11/steps/7/2.JPG)

We now have enough information to make predictions for the training data or even a new
dataset.

