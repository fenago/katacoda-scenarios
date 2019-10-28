Bootstrap Aggregation (or Bagging for short), is a simple and very powerful ensemble method.
An ensemble method is a technique that combines the predictions from multiple machine learning
algorithms together to make more accurate predictions than any individual model. Bootstrap
Aggregation is a general procedure that can be used to reduce the variance for those algorithms
that have high variance. An algorithm that has high variance are decision trees, like classification
and regression trees (CART).

Decision trees are sensitive to the specific data on which they are trained. If the training
data is changed (e.g. a tree is trained on a subset of the training data) the resulting decision
tree can be quite different and in turn the predictions can be quite different. Bagging is the
application of the Bootstrap procedure to a high-variance machine learning algorithm, typically
decision trees. Let’s assume we have a dataset of 1000 instances and we are using the CART
algorithm. Bagging of the CART algorithm would work as follows.
1. Create many (e.g. 100) random subsamples of our dataset with replacement.
2. Train a CART model on each sample.
3. Given a new dataset, calculate the average prediction from each model.