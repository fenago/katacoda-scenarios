<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab
# reshape 1D array to 2D
from numpy import array
# define array
data = array([10, 20, 30, 40, 50, 60, 70, 80])
print(data.shape)
# reshape
data = data.reshape((data.shape[0], 1))
print(data.shape)
</pre>

