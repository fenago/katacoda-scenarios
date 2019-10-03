<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 4
# generate a sample of random gaussians
from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot
# seed the random number generator
seed(0)
# generate univariate observations
data = 2 * randn(100) + 20
# histogram of generated data
pyplot.hist(data, bins=100)
pyplot.show()
</pre>

