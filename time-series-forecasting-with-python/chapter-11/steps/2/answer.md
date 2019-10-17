<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# create and plot a random series
from random import seed
from random import randrange
from matplotlib import pyplot
seed(0)
series = [randrange(5) for i in range(100)]
pyplot.plot(series)
pyplot.show()
</pre>