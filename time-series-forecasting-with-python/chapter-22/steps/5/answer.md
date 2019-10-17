<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# autocorrelation plot of time series
from pandas import read_csv
from matplotlib import pyplot
from statsmodels.graphics.tsaplots import plot_acf
series = read_csv('routine-heat.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
plot_acf(series, lags=11)
pyplot.show()
</pre>

