<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 7
# create array with hstack
from numpy import array
from numpy import hstack
# create first array
arr1 = array([5,10,15,20])
print(arr1)
# create second array
arr2 = array([4,8,12,16])
print(arr2)
# create third array
arr3 = array([2,4,4,8])
print(arr3)
# create horizontal stack
arr4 = hstack((arr1, arr2, arr3))
print(arr4)
print(arr4.shape)
</pre>

