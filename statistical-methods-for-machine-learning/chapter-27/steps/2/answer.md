<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# generate related variables
from numpy.random import rand
from numpy.random import seed
from matplotlib import pyplot
# seed random number generator
seed(0)
# prepare data
data1 = rand(100) * 30
data2 = data1 + (rand(100) * 20)
# plot
pyplot.scatter(data1, data2)
pyplot.show()
</pre>