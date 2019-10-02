<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab
# tensor product
from numpy import array
from numpy import tensordot
# define first vector
A = array([2,4])
# define second vector
B = array([3,6])
# calculate tensor product
C = tensordot(A, B, axes=0)
print(C)

</pre>

