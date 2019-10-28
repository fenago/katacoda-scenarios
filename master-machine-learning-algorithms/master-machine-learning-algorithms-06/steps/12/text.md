The LDA model requires the estimation of statistics from the training data:

1. Mean of each input value for each class
2. Probability of an instance belong to each class.
3. Covariance for the input data for each class.


#### Calculate the Class Means
The mean can be calculated for each class using:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-06/steps/12/1.JPG)

Where x are the input values for a class and n is the total number of input values. You can
use the AVERAGE() function in you spreadsheet. The mean value of x for each class is:
- Y = 0: 4.975415507
- Y = 1: 20.08706292