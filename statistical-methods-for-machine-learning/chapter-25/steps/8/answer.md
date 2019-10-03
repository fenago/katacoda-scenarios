<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 4
# log-normal distribution
from numpy.random import seed
from numpy.random import randn
from numpy import exp
from matplotlib import pyplot
# seed the random number generator
seed(0)
# generate two sets of univariate observations
data = 2 * randn(100) + 5
# transform to be exponential
data = exp(data)
# histogram
pyplot.hist(data)
pyplot.show()
</pre>

