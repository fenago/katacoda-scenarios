<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 6
# Example of Calculating the Root Mean Squared Error
from math import sqrt

# Calculate root mean squared error
def rmse_metric(actual, predicted):
	sum_error = 0.0
	for i in range(len(actual)):
		prediction_error = predicted[i] - actual[i]
		sum_error += (prediction_error ** 2)
	mean_error = sum_error / float(len(actual))
	return sqrt(mean_error)

# Test RMSE
actual = [0.2, 0.3, 0.4, 0.5, 0.6]
predicted = [0.21, 0.29, 0.49, 0.31, 0.4]
rmse = rmse_metric(actual, predicted)
print(rmse)
</pre>

