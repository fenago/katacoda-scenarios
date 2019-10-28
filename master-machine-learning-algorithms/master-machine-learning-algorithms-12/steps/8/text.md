KNN uses a distance measure to locate the k most similar instances from the training dataset
when making a prediction. The distance measure selected must respect the structure of the
problem so that data instances that are close to each other according to the distance measure
also belong to the same class. The most common distance measure for real values that have the
same units or scale is the Euclidean distance. Euclidean distance is calculated as the square root
of the sum of the squared differences between a point a and point b across all input attributes i.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-12/steps/8/1.JPG)

To make this concrete, we will work through the calculation of the Euclidean distance for
two instances from our dataset.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-12/steps/8/2.JPG)

