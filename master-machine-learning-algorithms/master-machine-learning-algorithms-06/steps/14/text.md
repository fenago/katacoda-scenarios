
Now we need to calculate the variance for the input variable for each class. You can understand
the variance as the difference of each instance from the mean. The difference is squared so
the variance is often written to include these units. It does not mean you need to square the
variance value when using it. We can calculate the variance for our dataset in two steps:

1. Calculate the squared difference for each input variable from the group mean.
2. Calculate the mean of the squared difference.

We can divide the dataset into two groups by the Y values 0 and 1. We can then calculate
the difference for each input value X from the mean from that group. We can calculate the
difference of each input value from the mean using:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-06/steps/14/1.JPG)
