
The first step is to calculate the squared difference for each attribute:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-12/steps/9/1.JPG)

We calculate the sum of these squared differences as:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-12/steps/9/2.JPG)

Finally, we need to take the square root of the sum. This will convert the units of the
difference between the data instances (real vectors) from squared units to their original units.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-12/steps/9/3.JPG)

This final step can be skipped for performance reasons. You probably don’t need the distance
in the actual units, and the square root function is relatively expensive compared to other
operations and will be performed many times per new data instance that is to be classified.
Now that you know how the Euclidean distance measure is calculated, we can use it with the
dataset to make predictions for new data.