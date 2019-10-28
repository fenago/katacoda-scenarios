
**KNN for Regression**

When KNN is used for regression problems the prediction is based on the mean or the median
of the k-most similar instances

**KNN for Classification**

When KNN is used for classification, the output can be calculated as the class with the highest
frequency from the k-most similar instances. Each instance in essence votes for their class and
the class with the most votes is taken as the prediction. Class probabilities can be calculated
as the normalized frequency of samples that belong to each class in the set of k most similar
instances for a new data instance. For example, in a binary classification problem (class is 0 or 1):

If you are using k and you have an even number of classes (e.g. 2) it is a good idea to choose
a k value with an odd number to avoid a tie. And the inverse, use an even number for k when
you have an odd number of classes. Ties can be broken consistently by expanding k by 1 and
looking at the class of the next most similar instance in the training dataset


**Curse of Dimensionality**

KNN works well with a small number of input variables (p), but struggles when the number
of inputs is very large. Each input variable can be considered a dimension of a p-dimensional
input space. For example, if you had two input variables X1 and X2, the input space would be
2-dimensional. As the number of dimensions increases the volume of the input space increases
at an exponential rate. In high dimensions, points that may be similar may have very large
distances. All points will be far away from each other and our intuition for distances in simple
2 and 3-dimensional spaces breaks down. This might feel unintuitive at first, but this general
problem is called the Curse of Dimensionality