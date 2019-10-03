<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab in Step 3
# histogram plot
from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot
# seed the random number generator
seed(0)
# generate univariate observations
data = 2 * randn(100) + 30
# histogram plot
pyplot.hist(data)
pyplot.show()

</pre>
