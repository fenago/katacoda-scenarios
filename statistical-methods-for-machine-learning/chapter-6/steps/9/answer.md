<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 7
# seed the pseudorandom number generator
from numpy.random import seed
from numpy.random import rand
# seed random number generator
seed(0)
# generate some random numbers
print(rand(5))
# reset the seed
seed(0)
# generate some random numbers
print(rand(5))

</pre>

