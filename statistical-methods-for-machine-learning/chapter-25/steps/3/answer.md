<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab in Step 3
# histogram plot of a large sample
from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot
# seed the random number generator
seed(0)
# generate a univariate data sample
data = 5 * randn(100) + 55
# histogram
pyplot.hist(data)
pyplot.show()
</pre>
