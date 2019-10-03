<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# idealized population distribution
from numpy import arange
from matplotlib import pyplot
from scipy.stats import norm
# x-axis for the plot
xaxis = arange(10, 80, 5)
# y-axis for the plot
yaxis = norm.pdf(xaxis, 40, 4)
# plot ideal population
pyplot.plot(xaxis, yaxis)
pyplot.show()

</pre>