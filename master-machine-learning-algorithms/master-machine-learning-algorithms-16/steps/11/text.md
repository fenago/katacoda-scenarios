Now we can create our second weak model from the weighted training instances. This second
model will also be a decision stump, but this time it will make a split on the X2 variable at the
value 2.122873405. Again, this is a contrived model intended to have poor accuracy. Ideally,
you would use something like the CART algorithm and the Gini index to choose a good quality
split point. It should be noted that the CART algorithm would take the instance weight into
account and focus on splitting at instances with a larger weight to result in a different decision
stump. If not, the algorithm will create the same decision stump in model after model and there
would be no chance to correct the predictions made from prior models. We will go through the
same process using this new split point.
- IF X2 ≤ 2.122873405 THEN **LEFT**
- IF X2 > 2.122873405 THEN **RIGHT**

This results in the following groups:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-16/steps/11/1.JPG)

Looking at the composition for each group, the LEFT group has the class value 1 and the
RIGHT group has the class value 0.31.5. Decision Stump: Model #3 146
- **LEFT**: Class 1
- **RIGHT**: Class 0

Using this simple decision tree, we can now calculate a prediction for each training instance
and the error and the weighted error for those predictions.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-16/steps/11/2.JPG)

A quick back of the envelope check indicates that this model was 80% accurate on the
training data. Slightly worse than the first model. It also looks like it made different mistakes
and correctly predicted the instances that the first model predicted incorrectly. We can calculate
the stage value for this classifier:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-16/steps/11/3.JPG)

We are not done yet. If we stop there, we will not have a very accurate AdaBoost model. In
fact a quick check suggests the model will only have an accuracy of 60% on the training data.
You can check this yourself later by changing the next section to only combine the predictions
from the first two models. We need one more model to make some final corrections.