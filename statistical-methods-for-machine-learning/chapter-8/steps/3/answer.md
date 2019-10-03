<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab in Step 3
# demonstration of the central limit theorem
from numpy.random import seed
from numpy.random import randint
from numpy import mean
from matplotlib import pyplot
# seed the random number generator
seed(0)
# calculate the mean of 20 dice rolls 100 times
means = [mean(randint(2, 5, 20)) for _ in range(100)]
# plot the distribution of sample means
pyplot.hist(means)
pyplot.show()
</pre>
