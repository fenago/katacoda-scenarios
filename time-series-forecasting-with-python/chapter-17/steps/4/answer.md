<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# calculate mean absolute error
from sklearn.metrics import mean_absolute_error
expected = [0.1, 0.4, 0.2, 0.4, 0.3]
predictions = [0.3, 0.5, 0.2, 0.5, 0.1]
mae = mean_absolute_error(expected, predictions)
print('MAE: %f' % mae)
</pre>

