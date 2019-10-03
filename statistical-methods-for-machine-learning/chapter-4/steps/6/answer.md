<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 6
# calculate the median of a sample
from numpy.random import seed
from numpy.random import randn
from numpy import median
# seed the random number generator
seed(0)
# generate univariate observations
data = 2 * randn(100) + 20
# calculate median
result = median(data)
print('Median: %.3f' % result)
</pre>

