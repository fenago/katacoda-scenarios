We can repeat this process and update the model for each training instance in the dataset. A
single iteration through the training dataset is called an epoch. It is common to repeat the
stochastic gradient descent procedure for a fixed number of epochs. At the end of epoch you
can calculate error values for the model. Because this is a classification problem, it would be
nice to get an idea of how accurate the model is at each iteration. The graph below show a plot
of accuracy of the model over 10 epochs.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-05/steps/7/1.JPG)

You can see that the model very quickly achieves 100% accuracy on the training dataset.
The coefficients calculated after 10 epochs of stochastic gradient descent are:

```
B0 = −0.406605464
B1 = 0.852573316
B2 = −1.104746259
```
