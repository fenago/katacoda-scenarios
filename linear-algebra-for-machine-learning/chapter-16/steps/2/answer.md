<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# singular-value decomposition
from numpy import array
from scipy.linalg import svd
# define a matrix
A = array([
	[2, 4],
	[3, 6],
	[4, 4]])
print(A)
# factorize
U, s, VT = svd(A)
print(U)
print(s)
print(VT)

</pre>