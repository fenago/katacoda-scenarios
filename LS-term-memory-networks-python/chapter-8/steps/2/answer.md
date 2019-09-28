<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
from numpy import zeros
from random import randint
from random import random
from matplotlib import pyplot

# generate the next frame in the sequence
def next_frame(last_step, last_frame, column):
	# define the scope of the next step
	lower = max(0, last_step-1)
	upper = min(last_frame.shape[0]-1, last_step+1)
	# choose the row index for the next step
	step = randint(lower, upper)
	# copy the prior frame
	frame = last_frame.copy()
	# add the new step
	frame[step, column] = 1
	return frame, step

# generate a sequence of frames of a dot moving across an image
def build_frames(size):
	frames = list()
	# create the first frame
	frame = zeros((size,size))
	step = randint(0, size-1)
	# decide if we are heading left or right
	right = 1 if random() < 0.5 else 0
	col = 0 if right else size-1
	frame[step, col] = 1
	frames.append(frame)
	# create all remaining frames
	for i in range(1, size):
		col = i if right else size-1-i
		frame, step = next_frame(step, frame, col)
		frames.append(frame)
	return frames, right

# generate sequence of frames
size = 6
frames, right = build_frames(size)
# plot all frames
pyplot.figure()
for i in range(size):
	# create a gray scale subplot for each frame
	pyplot.subplot(1, size, i+1)
	pyplot.imshow(frames[i], cmap='Greys')
	# turn of the scale to make it clearer
	ax = pyplot.gca()
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)
# show the plot
pyplot.show()

</pre>