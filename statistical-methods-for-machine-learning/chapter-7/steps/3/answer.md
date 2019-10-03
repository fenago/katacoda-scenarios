<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab in Step 3
# demonstrate the law of large numbers
from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import array
from matplotlib import pyplot
# seed the random number generator
seed(0)
# sample sizes
sizes = list()
for x in range (10, 20000, 20):
    sizes.append(x)
# generate samples of different sizes and calculate their means
means = [mean(10 * randn(size) + 100) for size in sizes]
# plot sample mean error vs sample size
pyplot.scatter(sizes, array(means)-50)
pyplot.show()

</pre>
