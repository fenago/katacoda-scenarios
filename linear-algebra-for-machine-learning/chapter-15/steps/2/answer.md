<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# eigendecomposition
from numpy import array
from numpy.linalg import eig
# define matrix
A = array([
	[2, 4, 6],
	[3, 6, 9],
	[4, 8, 9]])
print(A)
# factorize
values, vectors = eig(A)
print(values)
print(vectors)

</pre>