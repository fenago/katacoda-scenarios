<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 6
# tensor division
from numpy import array
# define first tensor
A = array([
  [[2,4,6],    [3,6,9],    [4,8,12]],
  [[5,10,15], [10,20,30], [6,12,18]],
  [[20,30,40], [11,22,33], [5,25,75]]])
# define second tensor
B = array([
  [[1,2,3],    [2,4,6],    [3,6,9]],
  [[4,8,12], [5,10,15], [10,20,30]],
  [[6,12,18], [20,30,40], [11,22,33]]])
# divide tensors
C = A / B
print(C)

</pre>

