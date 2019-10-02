<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab
# svd data reduction in scikit-learn
from numpy import array
from sklearn.decomposition import TruncatedSVD
# define matrix
A = array([
	[2,4,6,8,10,12,14,16,18,20],
	[3,6,9,12,15,18,21,24,27,30],
	[5,10,15,20,25,30,35,40,45,50]])
print(A)
# create transform
svd = TruncatedSVD(n_components=2)
# fit transform
svd.fit(A)
# apply transform
result = svd.transform(A)
print(result)
</pre>

