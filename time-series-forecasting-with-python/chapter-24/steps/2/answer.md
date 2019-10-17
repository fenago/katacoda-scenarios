<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# load and plot dataset
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
# load dataset
def parser(x):
	return datetime.strptime('201'+x, '%Y-%m')
series = read_csv('haircare-business.csv', header=0, index_col=0, parse_dates=True, squeeze=True, date_parser=parser)
# summarize first few rows
print(series.head())
# line plot
series.plot()
pyplot.show()
</pre>