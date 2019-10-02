<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# confirm eigenvector
from numpy import array
from numpy.linalg import eig
# define matrix
A = array([
	[2, 4, 6],
	[3, 6, 9],
	[4, 8, 9]])
# factorize
values, vectors = eig(A)
# confirm first eigenvector
B = A.dot(vectors[:, 0])
print(B)
C = vectors[:, 0] * values[0]
print(C)

</pre>
