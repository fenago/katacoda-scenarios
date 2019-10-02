<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# triangular matrices
from numpy import array
from numpy import tril
from numpy import triu
# define square matrix
M = array([
	[2, 4, 6],
	[3, 6, 9],
	[4, 8, 12]])
print(M)
# lower triangular matrix
lower = tril(M)
print(lower)
# upper triangular matrix
upper = triu(M)
print(upper)

</pre>