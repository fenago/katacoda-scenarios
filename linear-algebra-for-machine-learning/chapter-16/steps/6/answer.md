<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 6
# pseudoinverse via svd
from numpy import array
from numpy.linalg import svd
from numpy import zeros
from numpy import diag
# define matrix
A = array([
	[2, 3],
	[4, 9],
	[6, 12],
	[8, 15]])
print(A)
# factorize
U, s, VT = svd(A)
# reciprocals of s
d = 1.0 / s
# create m x n D matrix
D = zeros(A.shape)
# populate D with n x n diagonal matrix
D[:A.shape[1], :A.shape[1]] = diag(d)
# calculate pseudoinverse
B = VT.T.dot(D.T).dot(U.T)
print(B)
</pre>

