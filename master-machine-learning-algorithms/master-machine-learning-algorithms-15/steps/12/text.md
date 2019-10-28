Now that we have predictions from the bootstrap models we can aggregate the predictions into
an ensemble prediction. We can do that by taking the mode of each models prediction for each
training instance. The mode is a statistical function that select the most common value. In this
case, the most common class value predicted. Using this simple procedure we get the following
predictions:

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-15/steps/12/1.JPG)

You can see that all 10 training instances were classified correctly at 100% accuracy.