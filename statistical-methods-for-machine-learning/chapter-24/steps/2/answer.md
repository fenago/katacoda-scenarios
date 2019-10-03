<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# generate gaussian data
from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import std
# seed the random number generator
seed(0)
# generate univariate observations
data = 2 * randn(100) + 30
# summarize
print('mean=%.3f stdv=%.3f' % (mean(data), std(data)))

</pre>