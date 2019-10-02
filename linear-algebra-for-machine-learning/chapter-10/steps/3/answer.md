<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab in Step 3
# diagonal matrix
from numpy import array
from numpy import diag
# define square matrix
M = array([
	[2, 4, 6],
	[3, 6, 9],
	[4, 8, 12]])
print(M)
# extract diagonal vector
d = diag(M)
print(d)
# create diagonal matrix from vector
D = diag(d)
print(D)
</pre>
