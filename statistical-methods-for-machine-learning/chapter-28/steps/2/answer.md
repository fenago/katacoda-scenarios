<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# generate data samples
from numpy.random import seed
from numpy.random import rand
# seed the random number generator
seed(0)
# generate two sets of univariate observations
data1 = 30 + (rand(100) * 5)
data2 = 31 + (rand(100) * 5)
# summarize
print('data1: min=%.3f max=%.3f' % (min(data1), max(data1)))
print('data2: min=%.3f max=%.3f' % (min(data2), max(data2)))

</pre>