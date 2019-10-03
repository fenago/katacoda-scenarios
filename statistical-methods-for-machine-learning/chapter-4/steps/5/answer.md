<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 5
# calculate the mean of a sample
from numpy.random import seed
from numpy.random import randn
from numpy import mean
# seed the random number generator
seed(0)
# generate univariate observations
data = 2 * randn(100) + 20
# calculate mean
result = mean(data)
print('Mean: %.3f' % result)
</pre>

