<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab in Step 3
# invert matrix
from numpy import array
from numpy.linalg import inv
# define matrix
A = array([
	[2.0, 4.0],
	[3.0, 3.0]])
print(A)
# invert matrix
B = inv(A)
print(B)
# multiply A and B
I = A.dot(B)
print(I)

</pre>
