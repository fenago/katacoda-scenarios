<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab
# covariance matrix
from numpy import array
from numpy import cov
# define matrix of observations
X = array([
	[2, 3, 4],
	[4, 6, 8],
	[6, 9, 12],
	[8, 12, 16],
	[10, 15, 20]])
print(X)
# calculate covariance matrix
Sigma = cov(X.T)
print(Sigma)
</pre>

