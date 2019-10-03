<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 4
# example of a box and whisker plot
from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot
# seed the random number generator
seed(0)
# random numbers drawn from a Gaussian distribution
x = [randn(100), 15 * randn(100), 10 * randn(100)]
# create box and whisker plot
pyplot.boxplot(x)
# show line plot
pyplot.show()
</pre>

