<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# sparse matrix
from numpy import array
from scipy.sparse import csr_matrix
# create dense matrix
A = array([
	[1, 1, 1, 0, 0, 0],
	[0, 2, 2, 0, 2, 2],
	[0, 3, 3, 1, 0, 1]])
print(A)
# convert to sparse matrix (CSR method)
S = csr_matrix(A)
print(S)
# reconstruct dense matrix
B = S.todense()
print(B)

</pre>