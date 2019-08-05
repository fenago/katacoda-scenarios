To complete this step, create a function named mae_metric() that implements this metric. It expects
a list of actual outcome values and a list of predictions and use the built-in abs() Python function to calculate the absolute error values that are summed together.

<pre class="file" data-filename="mean_absolute_error.py" data-target="replace">

# Example of Calculating Mean Absolute Error

# Calculate mean absolute error
def mae_metric(actual, predicted):
    # Write code here

</pre>

We can contrive a small regression dataset to test this function.

<pre class="file" data-filename="mean_absolute_error.py">

# Test RMSE
actual = [0.1, 0.2, 0.3, 0.4, 0.5]
predicted = [0.11, 0.19, 0.29, 0.41, 0.5]
mae = mae_metric(actual, predicted)
print(mae)

</pre>

Now, run the python code by running: `python mean_absolute_error.py`{{execute}}

Only one prediction (0.5) is correct, whereas all other predictions are wrong by 0.01. Therefore,
we would expect the mean absolute error (or the average positive error) for these predictions to
be a little less than 0.01. 