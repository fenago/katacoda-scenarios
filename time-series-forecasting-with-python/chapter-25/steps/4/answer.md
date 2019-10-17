<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# PACF plot of time series
from pandas import read_csv
from matplotlib import pyplot
from statsmodels.graphics.tsaplots import plot_pacf
series = read_csv('routine-heat.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
plot_pacf(series, lags=30)
pyplot.show()
</pre>

