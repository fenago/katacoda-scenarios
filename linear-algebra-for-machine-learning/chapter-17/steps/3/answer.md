<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# matrix means
from numpy import array
from numpy import mean
# define matrix
M = array([
	[5,10,15,20,25,30,35,40],
	[2,4,6,8,10,12,14,16]])
print(M)
# column means
col_mean = mean(M, axis=0)
print(col_mean)
# row means
row_mean = mean(M, axis=1)
print(row_mean)

</pre>
