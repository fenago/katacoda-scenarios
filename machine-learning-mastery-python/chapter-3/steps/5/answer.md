<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 5
# pandas crash course


# series
import numpy
import pandas
array = numpy.array([10, 20, 30, 40])
rownames = ['w','x', 'y', 'z']
series = pandas.Series(array, index=rownames)
print(series)

print(series[2])
print(series['z'])


# dataframe
import numpy
import pandas
array = numpy.array([[10, 20, 30, 60], [40, 50, 60, 150]])
rownames = ['x', 'y']
colnames = ['first', 'second', 'third', 'fourth']
dataframe = pandas.DataFrame(array, index=rownames, columns=colnames)
print(dataframe)

print("second column: %s" % dataframe['second'])
print("third column: %s" % dataframe.third)

</pre>

