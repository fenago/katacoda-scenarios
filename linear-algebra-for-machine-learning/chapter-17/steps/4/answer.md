<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab
# vector variance
from numpy import array
from numpy import var
# define vector
v = array([5,10,15,20,25,30])
print(v)
# calculate variance
result = var(v, ddof=1)
print(result)
</pre>

