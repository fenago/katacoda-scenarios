<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# Plot of images as baseline for comparison
from keras.datasets import mnist
from matplotlib import pyplot
# load data
(X_train, y_train), (X_test, y_test) = mnist.load_data()
# create a grid of 3x2 images
for i in range(0, 6):
	pyplot.subplot(230 + 1 + i)
	pyplot.imshow(X_train[i], cmap=pyplot.get_cmap('Blues'))

# show the plot
pyplot.show()

</pre>