<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 5
# broadcasting error
from numpy import array
# define two-dimensional array
A = array([
	[5, 10, 15, 20],
	[10, 20, 30, 40]])
print(A.shape)
# define one-dimensional array
b = array([1, 2, 3])
print(b.shape)
# attempt broadcast
C = A + b
print(C)

</pre>

