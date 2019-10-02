<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 5
# pseudoinverse
from numpy import array
from numpy.linalg import pinv
# define matrix
A = array([
	[2, 3],
	[4, 9],
	[6, 12],
	[8, 15]])
print(A)
# calculate pseudoinverse
B = pinv(A)
print(B)
</pre>

