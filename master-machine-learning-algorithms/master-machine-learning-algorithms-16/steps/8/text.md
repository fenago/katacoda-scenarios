In this section we are going to learn an AdaBoost model from the training data. This will involve
learning 3 models, one after the other so that we can observe the effect on the weightings to the
training instances and how the predictions from each of the two models are combined. AdaBoost
uses decision stump (one node decision trees) as the internal model. Rather than using the
CART algorithm or similar to choose the split points for these decision trees, we will select split
points manually. Again, these split points will be picked poorly to create classification errors
and to demonstrate how the second model can correct the first model, and so on.

#### Decision Stump: Model #1
The first model will be a decision stump for the X1 input variable split at the value 4.932600453.
- IF X1 ≤ 4:932600453 THEN **LEFT**
- IF X1 > 4:932600453 THEN **RIGHT**
This is a poor split point for this data and was chosen intentionally for this tutorial to
create some misclassified instances. Ideally, you would use the CART algorithm to choose a
split point for this dataset with the Gini index as a cost function. If we apply this split point to
the training data we can see the data split into the following two groups:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-16/steps/8/1.JPG)

Looking at the composition of this group, we can see that the right group is predominately
in class 1 and the left group is predominately class 0. These class values will be the predictions
made for each group.
- **LEFT**: Class 0
- **RIGHT**: Class 1

Now that we have a decision stump model trained, we can use it to make predictions for the
training dataset. The error in the prediction can be calculated using:
- error = 0 IF Prediction == Y
- error = 1 IF Prediction != Y

We can summarize the predictions using the decision stump and their errors in the table
below.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-16/steps/8/2.JPG)