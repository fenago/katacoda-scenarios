<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# QR decomposition
from numpy import array
from numpy.linalg import qr
# define rectangular matrix
A = array([
	[2, 4],
	[3, 6],
	[4, 8]])
print(A)
# factorize
Q, R = qr(A, 'complete')
print(Q)
print(R)
# reconstruct
B = Q.dot(R)
print(B)

</pre>
