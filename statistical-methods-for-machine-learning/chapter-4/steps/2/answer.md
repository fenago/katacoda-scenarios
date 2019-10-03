<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# generate and plot an idealized gaussian
from numpy import arange
from matplotlib import pyplot
from scipy.stats import norm
# x-axis for the plot
x_axis = arange(-4, 4, 1.011)
# y-axis as the gaussian
y_axis = norm.pdf(x_axis, 1, 1)
# plot data
pyplot.plot(x_axis, y_axis)
pyplot.show()
</pre>