<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# calculate mean forecast error
expected = [0.1, 0.4, 0.2, 0.4, 0.3]
predictions = [0.3, 0.5, 0.2, 0.5, 0.1]
forecast_errors = [expected[i]-predictions[i] for i in range(len(expected))]
bias = sum(forecast_errors) * 1.0/len(expected)
print('Bias: %f' % bias)

</pre>
