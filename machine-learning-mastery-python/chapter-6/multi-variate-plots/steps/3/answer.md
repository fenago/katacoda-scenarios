<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab in Step 3
# Scatterplot Matrix

from matplotlib import pyplot
from pandas import read_csv
from pandas.plotting import scatter_matrix
filename = "pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
scatter_matrix(data)
pyplot.show()

</pre>
