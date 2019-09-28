<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 5
# Example of Calculating Mean Absolute Error

# Calculate mean absolute error
def mae_metric(actual, predicted):
    sum_error = 0.0
    for i in range(len(actual)):
        sum_error += abs(predicted[i] - actual[i])
    return sum_error / float(len(actual))

# Test RMSE
actual = [0.2, 0.3, 0.4, 0.5, 0.6]
predicted = [0.21, 0.29, 0.49, 0.31, 0.4]
mae = mae_metric(actual, predicted)
print(mae)
</pre>

