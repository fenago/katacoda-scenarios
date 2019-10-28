There are many other distance measures that can be used, such as Tanimoto, Jaccard,
Mahalanobis and cosine distance. You can choose the best distance metric based on the
properties of your data. If you are unsure, you can experiment with different distance metrics
and different values of k together and see which mix results in the most accurate models.
Euclidean is a good distance measure to use if the input variables are similar in type (e.g.
all measured widths and heights). Manhattan distance is a good measure to use if the input
variables are not similar in type (such as age, gender, height, etc.).

The value for k can be found by algorithm tuning. It is a good idea to try many different
values for k (e.g. values from 1 to 21) and see what works best for your problem. The
computational complexity of KNN increases with the size of the training dataset. For very large
training sets, KNN can be made stochastic by taking a sample from the training dataset from
which to calculate the k-most similar instances. KNN has been around for a long time and has
been very well studied. As such, different disciplines have different names for it, for example:

- **Instance-Based Learning:** The raw training instances are used to make predictions. As
such KNN is often referred to as instance-based learning or a case-based learning (where
each training instance is a case from the problem domain).
- **Lazy Learning:** No learning of the model is required and all of the work happens at
the time a prediction is requested. As such, KNN is often referred to as a lazy learning
algorithm.
- **Nonparametric:** KNN makes no assumptions about the functional form of the problem
being solved. As such KNN is referred to as a nonparametric machine learning algorithm.
KNN can be used for regression and classification problems.

