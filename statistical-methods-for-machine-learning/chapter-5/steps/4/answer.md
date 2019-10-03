<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 4
# example of a histogram plot
from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot
# seed the random number generator
seed(0)
# random numbers drawn from a Gaussian distribution
x = randn(100)
# create histogram plot
pyplot.hist(x)
# show line plot
pyplot.show()
</pre>

