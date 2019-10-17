<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# calculate mean squared error
from sklearn.metrics import mean_squared_error
expected = [0.1, 0.4, 0.2, 0.4, 0.3]
predictions = [0.3, 0.5, 0.2, 0.5, 0.1]
mse = mean_squared_error(expected, predictions)
print('MSE: %f' % mse)
</pre>

