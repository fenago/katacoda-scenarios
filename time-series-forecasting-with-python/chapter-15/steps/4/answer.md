<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# plot a histogram of a time series
from pandas import read_csv
from matplotlib import pyplot
series = read_csv('routine-births.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
series.hist()
pyplot.show()
</pre>

