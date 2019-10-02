<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab
# vector covariance
from numpy import array
from numpy import cov
# define first vector
x = array([5,10,15,20,25,30,35,40,45])
print(x)
# define second covariance
y = array([45,40,35,30,25,20,15,10,5])
print(y)
# calculate covariance
Sigma = cov(x,y)[0,1]
print(Sigma)
</pre>

