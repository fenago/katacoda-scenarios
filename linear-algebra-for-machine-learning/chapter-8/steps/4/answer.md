<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 4
# vector max norm
from numpy import inf
from numpy import array
from numpy.linalg import norm
# define vector
a = array([10, 20, 30, 40, 50])
print(a)
# calculate norm
maxnorm = norm(a, inf)
print(maxnorm)
</pre>

