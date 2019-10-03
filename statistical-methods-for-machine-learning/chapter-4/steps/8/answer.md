<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 7
# calculate the variance of a sample
from numpy.random import seed
from numpy.random import randn
from numpy import var
# seed the random number generator
seed(0)
# generate univariate observations
data = 2 * randn(100) + 20
# calculate variance
result = var(data)
print('Variance: %.3f' % result)
</pre>

