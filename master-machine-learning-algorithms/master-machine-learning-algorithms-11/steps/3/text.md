A simple dataset was contrived for our purposes. It is comprised of two input variables X1 and
X2 and one output variable Y . The input variables are drawn from a Gaussian distribution,
which is one assumption made by Gaussian Naive Bayes. The class variable has two values, 0
and 1, therefore the problem is a binary classification problem.
Data from class 0 was drawn randomly from a Gaussian distribution with a standard
deviation of 1.0 for X1 and X2. Data from class 1 was drawn randomly from a Gaussian
distribution with a mean of 7.5 for X1 and 2.5 for X2. This means that the classes are nicely
separated if we plot the input data on a scatter plot. The raw dataset is listed below:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-11/steps/3/1.JPG)

You can clearly see the separation of the classes in the plot below. This will make the data
relatively easy to work with as we implement and test a Gaussian Naive Bayes model.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-11/steps/3/2.JPG)
