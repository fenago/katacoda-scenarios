We can calculate an error score for our predictions called the Root Mean Squared Error or `RMSE`.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-02/steps/10/1.JPG)

Where you can use SQRT() function in your spreadsheet to calculate the square root, p is the
predicted value and y is the actual value, i is the index for a specific instance, because we must
calculate the error across all predicted values. First we must calculate the difference between
each model prediction and the actual y values.

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-02/steps/10/2.JPG)

We can easily calculate the square of each of these error values (error × error or error2).

![](https://github.com/fenago/katacoda-scenarios/raw/master/master-machine-learning-algorithms/master-machine-learning-algorithms-02/steps/10/3.JPG)

The sum of these errors is 2.4 units, dividing by 5 and taking the square root gives us:

```
RMSE = 0.692820323
```

Or, each prediction is on average wrong by about 0.692 units.