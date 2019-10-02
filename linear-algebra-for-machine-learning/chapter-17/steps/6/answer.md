<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 6
# matrix standard deviation
from numpy import array
from numpy import std
# define matrix
M = array([
	[5,10,15,20,25,30],
	[2,4,6,8,10,12]])
print(M)
# column standard deviations
col_std = std(M, ddof=1, axis=0)
print(col_std)
# row standard deviations
row_std = std(M, ddof=1, axis=1)
print(row_std)
</pre>

