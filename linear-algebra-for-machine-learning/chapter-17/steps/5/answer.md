<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 5
# matrix variances
from numpy import array
from numpy import var
# define matrix
M = array([
	[5,10,15,20,25,30],
	[2,4,6,8,10,12]])
print(M)
# column variances
col_var = var(M, ddof=1, axis=0)
print(col_var)
# row variances
row_var = var(M, ddof=1, axis=1)
print(row_var)
</pre>

