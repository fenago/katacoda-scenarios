Let’s jump ahead. You can repeat this process another 19 times. This is 4 complete epochs of
the training data being exposed to the model and updating the coefficients. Here is a list of all
of the values for the coefficients over the 20 iterations that you should see:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-03/steps/8/1.JPG)

I think that 20 iterations or 4 epochs is a nice round number and a good place to stop.
You could keep going if you wanted. Your values should match closely, but may have minor
differences due to different spreadsheet programs and different precisions. You can plug each
pair of coefficients back into the simple linear regression equation. This is useful because we can
calculate a prediction for each training instance and in turn calculate the error.
Below is a plot of the error for each set of coefficients as the learning process unfolded. This
is a useful graph as it shows us that error was decreasing with each iteration and starting to
bounce around a bit towards the end.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-03/steps/8/2.JPG)
