To complete this step, create a function named cross_validation_split() to split a dataset.
Create a copy of the dataset from which to draw randomly chosen rows and calculate the size of
each fold as the size of the dataset divided by the number of folds required.<br/>
            fold size = count(rows)/count(folds) 

<pre class="file" data-filename="root_mean_squared_error.py" data-target="replace">

# Example of Calculating the Root Mean Squared Error
from math import sqrt

# Calculate root mean squared error
def rmse_metric(actual, predicted):
    # Write code here

</pre>

We can test this metric on the same dataset used to test the calculation of Mean Absolute
Error above. Below is an example. We would expect an error value to be
generally close to 0.01.

<pre class="file" data-filename="root_mean_squared_error.py">

# Test RMSE
actual = [0.1, 0.2, 0.3, 0.4, 0.5]
predicted = [0.11, 0.19, 0.29, 0.41, 0.5]
rmse = rmse_metric(actual, predicted)
print(rmse)

</pre>


Now, run the python code by running: `python root_mean_squared_error.py`{{execute}}