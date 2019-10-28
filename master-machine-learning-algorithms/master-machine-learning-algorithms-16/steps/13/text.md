We can now make predictions for the training dataset using the AdaBoost model. Predictions
for a single classifier are either +1 or -1 and weighted by the stage value for the model. For
example for this problem we will use:

`prediction = stage × (IF (output == 0) THEN −1 ELSE +1)`

Using the three models above, we can make weighted predictions given the input values
from the training data. This could just as easily be new data for which we would like to make
predictions

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-16/steps/13/2.JPG)

We can sum the predictions for each model to give a final outcome. If an outcome is less
than 0 then the 0 class is predicted, and if an outcome is greater than 0 the 1 class is predicted.
We can now calculate the final predictions from the AdaBoost model.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-16/steps/13/3.JPG)

We can see that the predictions match the expected Y values perfectly. Or stated another
way, the AdaBoost model achieved an accuracy of 100% on the training data.