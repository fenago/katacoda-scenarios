Again, we can update the weights for the instances using the same update procedure described
above. This gives us the following weights:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-16/steps/12/1.JPG)

This model will choose a split point for X2 at 0.862698005.
- IF X2 ≤ 0.862698005 THEN **LEFT**
- IF X2 > 0.862698005 THEN **RIGHT**

This split point separates the dataset into the following groups:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-16/steps/12/2.JPG)

Again, looking at the composition for each group, the LEFT group has the class value 1 and
the RIGHT group has the class value 0.
- **LEFT**: Class 1
- **RIGHT**: Class 0
Using this final simple decision tree, we can now calculate a prediction for each training
instance and the error and the weighted error for those predictions.

This model too makes 2 errors (or has an accuracy of 80%). Again, we can calculate the
stage value for this classifier:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-16/steps/12/3.JPG)

Now we are done. Let’s look at how we can use this series of boosted models to make
predictions.
