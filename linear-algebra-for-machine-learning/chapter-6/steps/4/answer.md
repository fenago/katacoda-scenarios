<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab
# broadcast one-dimensional array to two-dimensional array
from numpy import array
# define two-dimensional array
A = array([
	[5, 10, 15],
	[10, 20, 30]])
print(A)
# define one-dimensional array
b = array([5, 25, 75])
print(b)
# broadcast
c = A + b
print(c)
</pre>

