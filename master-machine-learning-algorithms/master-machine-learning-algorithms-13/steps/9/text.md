
We can calculate the distance between a training instance and a codebook vector using Euclidean
distance. This is the most common distance measure when all input attributes have the same
scale, which they do in this case. Euclidean distance is calculated as the square root of the sum
of the squared differences between a point a and point b across all input attributes i.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-13/steps/9/1.JPG)

Let’s calculate the Euclidean distance between each codebook vector and the training
instance. The results are listed below.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-13/steps/9/2.JPG)

From the distances, we can see that the codebook vector #1 has the smallest distance and
is therefore the BMU.