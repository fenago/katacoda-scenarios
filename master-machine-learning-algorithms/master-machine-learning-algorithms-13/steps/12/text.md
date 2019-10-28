Once the codebook vectors are learned, they can be used to make predictions. We can use the
same procedure as KNN to make predictions, although k is set to 1. Just like in the learning
process, we use a distance measure to locate the BMU for a new data instance. Instead of
updating the BMU, we return the class value which becomes the prediction for our model. Using
the codebook vectors prepared above, and the Euclidean distance measure, we can make the
following predictions for each instance in the dataset:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-13/steps/12/1.JPG)

If we compare this to the actual values in the dataset for Y , we can see some errors. The
classification accuracy can be calculated as:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-13/steps/12/2.JPG)

With some more training the codebook vectors will become more accurate.