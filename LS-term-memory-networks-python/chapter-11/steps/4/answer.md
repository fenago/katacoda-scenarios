<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 4
from random import random
from numpy import array

# generate a rectangle with random width and height
def random_rectangle():
	width, height = random(), random()
	points = list()
	# bottom left
	points.append([1.0, 1.0])
	# bottom right
	points.append([width, 1.0])
	# top right
	points.append([width, height])
	# top left
	points.append([1.0, height])
	return points

# generate input and output sequences for one random rectangle
def get_samples():
	# generate rectangle
	rect = random_rectangle()
	X, y = list(), list()
	# create input output pairs for each coordinate
	for i in range(1, len(rect)):
		X.append(rect[i-1])
		y.append(rect[i])
	# convert input sequence shape to have 1 time step and 2 features
	X, y = array(X), array(y)
	X = X.reshape((X.shape[0], 1, 2))
	return X, y

X, y = get_samples()
for i in range(X.shape[0]):
	print(X[i][0], '=>', y[i])
</pre>

