<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# query a dataset using a date-time index
from pandas import read_csv
series = read_csv('routine-births.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
print(series['1960-01'])
</pre>

