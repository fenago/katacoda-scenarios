Given a new data instance for which we would like to make a prediction, the k instances with
the smallest distance to the new data instance are chosen to contribute to that prediction. For
classification, this involves allowing each of the k members to vote of which class the new data
instance belongs. To make this concrete, we will work through making a prediction for a new
data instance using the training dataset as the model. The new data instance is listed below.
We are cheating because we contrived the dataset, we know what class the instance should be
allocated. 

```
Instance: X1 = 8:093607318, X2 = 3:365731514, Y = 1.
```

The first step is to calculate the Euclidean distance between the new input instance and
all instances in the training dataset. The table below lists the distance between each training
instance and the new data.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-12/steps/10/1.JPG)
