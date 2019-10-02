<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 5
# orthogonal matrix
from numpy import array
from numpy.linalg import inv
# define orthogonal matrix
Q = array([
	[2, 4],
	[3, -6]])
print(Q)
# inverse equivalence
V = inv(Q)
print(Q.T)
print(V)
# identity equivalence
I = Q.dot(Q.T)
print(I)
</pre>

