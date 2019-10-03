<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 4
# example of a scatter plot
from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot
# seed the random number generator
seed(0)
# first variable
x = 10 * randn(1000) + 10
# second variable
y = x + (15 * randn(1000) + 60)
# create scatter plot
pyplot.scatter(x, y)
# show line plot
pyplot.show()
</pre>

