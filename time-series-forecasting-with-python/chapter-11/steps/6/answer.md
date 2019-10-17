<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# calculate and plot a differenced random walk
from random import seed
from random import random
from matplotlib import pyplot
# create random walk
seed(0)
random_walk = list()
random_walk.append(-1 if random() < 0.5 else 1)
for i in range(1, 100):
	movement = -1 if random() < 0.5 else 1
	value = random_walk[i-1] + movement
	random_walk.append(value)
# take difference
diff = list()
for i in range(1, len(random_walk)):
	value = random_walk[i] - random_walk[i - 1]
	diff.append(value)
# line plot
pyplot.plot(diff)
pyplot.show()
</pre>

