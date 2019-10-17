<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# load time series data
from pandas import read_csv
from matplotlib import pyplot
series = read_csv('global-travelers.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
series.plot()
pyplot.show()

</pre>
