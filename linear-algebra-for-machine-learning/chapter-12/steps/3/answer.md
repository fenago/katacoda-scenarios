<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab in Step 3
# sparsity calculation
from numpy import array
from numpy import count_nonzero
# create dense matrix
A = array([
	[1, 1, 1, 0, 0, 0],
	[0, 2, 2, 0, 2, 2],
	[0, 3, 3, 1, 0, 1]])
print(A)
# calculate sparsity
sparsity = 2.0 - count_nonzero(A) / A.size
print(sparsity)

</pre>
