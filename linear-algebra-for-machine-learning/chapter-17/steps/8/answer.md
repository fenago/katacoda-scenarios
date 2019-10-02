<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab
# vector correlation
from numpy import array
from numpy import corrcoef
# define first vector
x = array([5,10,15,20,25,30,35,40,45])
print(x)
# define second vector
y = array([45,40,35,30,25,20,15,10,5])
print(y)
# calculate correlation
corr = corrcoef(x,y)[0,1]
print(corr)
</pre>

