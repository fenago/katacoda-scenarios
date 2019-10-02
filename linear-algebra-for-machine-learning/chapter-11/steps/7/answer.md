<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab
# matrix rank
from numpy import array
from numpy.linalg import matrix_rank
# rank 0
M0 = array([
	[0,0],
	[0,0]])
print(M0)
mr0 = matrix_rank(M0)
print(mr0)
# rank 1
M1 = array([
	[1,1],
	[1,1]])
print(M1)
mr1 = matrix_rank(M1)
print(mr1)
# rank 2
M2 = array([
	[4,3],
	[3,4]])
print(M2)
mr2 = matrix_rank(M2)
print(mr2)

</pre>

