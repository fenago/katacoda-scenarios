We are now ready to make predictions. Predictions are made by calculating the discriminant
function for each class and predicting the class with the largest value. The discriminant function
for a class given an input (x) is calculated using:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-06/steps/15/1.JPG)

Where x is the input value, mean, variance and probability are calculated above for the class
we are discriminating. After calculating the discriminant value for each class, the class with
the largest discriminant value is taken as the prediction. Let’s step through the calculation of
the discriminate value of each class for the first instance. The first instance in the dataset is:
X = 4:667797637 and Y = 0. The discriminant value for Y = 0 is calculated as follows:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-06/steps/15/2.JPG)

