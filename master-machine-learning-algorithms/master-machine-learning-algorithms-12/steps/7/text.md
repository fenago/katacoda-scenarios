The k-Nearest Neighbors (KNN) algorithm is very simple and very effective. In this chapter
you will discover exactly how to implement it from scratch, step-by-step. We will now learn:

- How to calculate the Euclidean distance between real valued vectors.
- How to use Euclidean distance and the training dataset to make predictions for new data.

Let’s get started.

#### Tutorial Dataset
The problem is a binary (two-class) classification problem. This problem was contrived for this
tutorial. The dataset contains two input variables (X1 and X2) and the class output variable
with the values 0 and 1. The dataset contains 10 records, 5 that belong to each class.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-12/steps/7/1.JPG)

You can see that the data for each class is quite separated. This is intentionally to make the
problem easy to work with so that we can focus on the learning algorithm.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-12/steps/7/2.JPG)
