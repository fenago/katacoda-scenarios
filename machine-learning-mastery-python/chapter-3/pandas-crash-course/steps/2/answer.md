<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 2
# Series

import numpy
import pandas
myarray = numpy.array([1, 2, 3])
rownames = ['a', 'b', 'c']
myseries = pandas.Series(myarray, index=rownames)
print(myseries)

#You can access the data in a series like a NumPy array and like a #dictionary, for example:

print(myseries[0])
print(myseries['a'])

</pre>