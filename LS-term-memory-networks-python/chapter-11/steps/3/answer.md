<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab in Step 3
from random import random
from matplotlib import pyplot
from matplotlib.patches import PathPatch
from matplotlib.path import Path

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

# plot a rectangle
def plot_rectangle(rect):
	# close the rectangle path
	rect.append(rect[0])
	# define path
	codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
	path = Path(rect, codes)
	axis = pyplot.gca()
	patch = PathPatch(path)
	# add shape to plot
	axis.add_patch(patch)
	axis.set_xlim(-0.1,1.1)
	axis.set_ylim(-0.1,1.1)
	pyplot.show()

rect = random_rectangle()
plot_rectangle(rect)

</pre>
