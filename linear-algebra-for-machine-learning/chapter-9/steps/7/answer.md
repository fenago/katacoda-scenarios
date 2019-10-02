<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab
# matrix dot product
from numpy import array
# define first matrix
A = array([
	[10, 20],
	[30, 40],
	[50, 60]])
print(A)
# define second matrix
B = array([
	[5, 10],
	[3, 6]])
print(B)
# multiply matrices
C = A.dot(B)
print(C)
# multiply matrices with @ operator
D = A @ B
print(D)
</pre>

