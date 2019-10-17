<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# upsample to daily intervals
from pandas import read_csv
from pandas import datetime

def parser(x):
	return datetime.strptime('201'+x, '%Y-%m')

series = read_csv('haircare-business.csv', header=0, index_col=0, parse_dates=True, squeeze=True, date_parser=parser)
upsampled = series.resample('D').mean()
print(upsampled.head(20))
</pre>