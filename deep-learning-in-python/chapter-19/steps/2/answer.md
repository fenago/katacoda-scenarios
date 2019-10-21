<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# Plot ad hoc mnist instances
from keras.datasets import mnist
import matplotlib.pyplot as plt
# load (downloaded if needed) the MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()
# plot 4 images as gray scale
plt.subplot(221)
plt.imshow(X_train[5], cmap=plt.get_cmap('Blues'))
plt.subplot(222)
plt.imshow(X_train[6], cmap=plt.get_cmap('Blues'))
plt.subplot(223)
plt.imshow(X_train[7], cmap=plt.get_cmap('Blues'))
plt.subplot(224)
plt.imshow(X_train[8], cmap=plt.get_cmap('Blues'))
# show the plot
plt.show()


</pre>