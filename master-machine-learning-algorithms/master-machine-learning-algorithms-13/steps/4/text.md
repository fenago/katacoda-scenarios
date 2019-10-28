Predictions are made using the LVQ codebook vectors in the same way as k-Nearest Neighbors.
Predictions are made for a new instance by searching through all codebook vectors for the k most
similar instances and summarizing the output variable for those k instances. For classification
this is the mode (or most common) class value. Typically predictions are made with k = 1, and
the codebook vector that matches is called the Best Matching Unit (BMU).
To determine which of the k instances in the training dataset are most similar to a new
input a distance measure is used. For real-valued input variables, the most popular distance
measure is Euclidean distance. Euclidean distance is calculated as the square root of the sum of
the squared differences between a point a and point b across all input attributes i.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-13/steps/4/1.JPG)
