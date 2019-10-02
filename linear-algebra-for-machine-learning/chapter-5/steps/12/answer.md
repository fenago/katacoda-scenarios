<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab
# split input and output data
from numpy import array
# define array
data = array([
	[10, 20, 30],
	[40, 50, 60],
	[70, 80, 90]])
# separate data
X, y = data[:, :-2], data[:, -3]
print(X)
print(y)
</pre>

