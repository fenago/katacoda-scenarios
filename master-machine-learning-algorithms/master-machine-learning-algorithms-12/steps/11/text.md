We will set k to 3 and choose the 3 most similar neighbors to the data instance. A value of
k = `3` is small and easy to use in this example, it is also an odd number, meaning that when the
neighbors vote on the output class, that we cannot have a tie. The k = 3 most similar neighbors
to the new data instance are:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-12/steps/11/1.JPG)

Making a prediction is as easy as selecting the majority class in the neighbors. Because we
are using 0 and 1 for the class values, we can use the MODE() statistical function in a spreadsheet
to return the most frequent value.

`prediction = mode(class(i))`

In this case all 3 neighbors have a class of 1, therefore the prediction for this instance is `1`,
which is `correct`.

#### Summary
In this chapter you discovered how you can use k-Nearest Neighbors to make predictions on a
binary classification problem. You learned about:
- The Euclidean distance measure and how to calculate it step-by-step.
- How to use the Euclidean distance to locate the nearest neighbors for a new data instance.
- How to make a prediction from the k-nearest neighbors.
You now know how to implement k-Nearest Neighbors from scratch for classification. 