Now that we have trained the model, we can use it to make predictions. We can make predictions
on the training dataset, but this could just as easily be new data. Using the coefficients above
learned after 10 epochs, we can calculate output values for each training instance:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-05/steps/8/1.JPG)

These are the probabilities of each instance belonging to Y = 0. We can convert these into
crisp class values using:

```
prediction = IF (output < 0.5) Then 0 Else 1
```

With this simple procedure we can convert all of the outputs to class values:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-05/steps/8/2.JPG)

Finally, we can calculate the accuracy for the model on the training dataset:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-05/steps/8/3.JPG)
