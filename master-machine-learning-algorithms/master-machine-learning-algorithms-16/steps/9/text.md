We can see 1 error in 10 predictions or an accuracy of 0.9 or 90%. Not bad, but not ideal.
When using AdaBoost, we calculate the misclassification rate for a weak model like the above
decision stump using the following equation:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-16/steps/9/1.JPG)

Each instance in the training dataset has the starting weight of N1 where N is the number of
training instance, in this case 10 so 1/10 = 0.1.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-16/steps/9/2.JPG)

Using this starting weight and the prediction errors above, we can calculate the weighted
error for each prediction.

`WeightedError = weight × error`

The results are listed below.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-16/steps/9/3.JPG)

Now we can calculate the misclassification rate as:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-16/steps/9/4.JPG)

Finally, we can use the misclassification rate to calculate the stage for this weak model. The
stage is the weight applied to any prediction made by this model later when we use it to actually
make predictions. The stage is calculated as:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-16/steps/9/5.JPG)

This classifier will have a lot of weight on predictions, which is good because it is 90%
accurate.