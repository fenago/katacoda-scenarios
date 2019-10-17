<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# additive decompose a contrived additive time series
from random import randrange
from matplotlib import pyplot
from statsmodels.tsa.seasonal import seasonal_decompose
series = [i+randrange(5) for i in range(1,1000)]
result = seasonal_decompose(series, model='additive', freq=1)
result.plot()
pyplot.show()
</pre>