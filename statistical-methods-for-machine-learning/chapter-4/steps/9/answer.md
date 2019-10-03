<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 7
# calculate the standard deviation of a sample
from numpy.random import seed
from numpy.random import randn
from numpy import std
# seed the random number generator
seed(0)
# generate univariate observations
data = 2 * randn(100) + 20
# calculate standard deviation
result = std(data)
print('Standard Deviation: %.3f' % result)

</pre>

