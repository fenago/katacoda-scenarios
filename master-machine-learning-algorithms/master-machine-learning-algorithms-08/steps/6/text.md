The CART model is learned by looking for split points in the data. A split point is a single
value of a single attribute, e.g. the first value of the X1 attribute 2.771244718. Partitioning
data at a split point involves separating all data at that node into two groups, left of the split
point and right of the split point. If we are working on the first split point in the tree, then all
of the dataset is affected. If we are working on say a split point one level deep, then only the
data that has filtered down the tree from nodes above and is sitting at that node is affected by
the split point.

We are not concerned with what the class value is of the chosen split point. We only care
about the composition of the data assigned to the LEFT and to the RIGHT child nodes of the
split point. A cost function is used to evaluate the mix of classes of training data assigned to
each side of the split. In classification problems the Gini index cost function is used.

