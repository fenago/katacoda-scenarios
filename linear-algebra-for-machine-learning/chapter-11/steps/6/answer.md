<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 6
# vector rank
from numpy import array
from numpy.linalg import matrix_rank
# rank
v1 = array([5, 10, 15, 20, 25])
print(v1)
vr1 = matrix_rank(v1)
print(vr1)
# zero rank
v2 = array([0,0,0,0,0])
print(v2)
vr2 = matrix_rank(v2)
print(vr2)

</pre>

