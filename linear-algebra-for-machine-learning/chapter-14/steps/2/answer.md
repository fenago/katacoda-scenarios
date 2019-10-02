<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# LU decomposition
from numpy import array
from scipy.linalg import lu
# define a square matrix
A = array([
	[2, 4, 6],
	[3, 6, 9],
	[4, 8, 9]])
print(A)
# factorize
P, L, U = lu(A)
print(P)
print(L)
print(U)
# reconstruct
B = P.dot(L).dot(U)
print(B)

</pre>