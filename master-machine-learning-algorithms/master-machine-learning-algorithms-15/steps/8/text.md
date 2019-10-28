Bootstrap Aggregation (or Bagging for short), is a simple and very powerful ensemble method.
Bagging works by taking a subsample of your training dataset (with replacement) and creating
a model, often a decision tree because they have high variance. The process is repeated creating
as many trees as you desire. Later when making predictions for new data, the outputs from
each tree are combined by taking the average.

Decision trees like CART select split points using a greedy algorithm that seeks to minimize
a cost function, like the Gini index for classification. When the tree is created on a random
sample of the training data, the algorithm is likely to choose different split points, resulting in
different trees and in turn different predictions. This is where the power for bagging comes from,
in combining the predictions from models that have very different perspectives on the problem.

The interesting part of bagged decision trees is how they are combined to make ensemble
predictions.With this in mind, we will contrive 3 decision trees from the training data, each
with sub-par accuracy. The split points were chosen manually to demonstrate exactly how
different perspectives on the same problem can be combined to provide increased performance.
A decision tree with one split point is called a decision stump, this is because there is little tree
to speak of. We will use three decision stumps. The split points for each are as follows:

```
Model1 : X1 ≤ 5:38660215
Model2 : X1 ≤ 4:090032824
Model3 : X2 ≤ 0.925340325
```
