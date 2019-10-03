<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 4
# histogram plot of data with a long tail
from numpy.random import seed
from numpy.random import randn
from numpy.random import rand
from numpy import append
from matplotlib import pyplot
# seed the random number generator
seed(0)
# generate a univariate data sample
data = 2 * randn(100) + 5
tail = 5 + (rand(500) * 10)
# add long tail
data = append(data, tail)
# histogram
pyplot.hist(data)
pyplot.show()
</pre>

