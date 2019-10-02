<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab 
# reshape 2D array to 3D
from numpy import array
# list of data
data = [[10, 20],
		[30, 40],
		[50, 60],
	    [70, 80],
       [90, 100]]
# array of data
data = array(data)
print(data.shape)
# reshape
data = data.reshape((data.shape[0], data.shape[1], 1))
print(data.shape)
</pre>

