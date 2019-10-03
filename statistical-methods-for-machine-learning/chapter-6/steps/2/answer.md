<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# seed the pseudorandom number generator
from random import seed
from random import random
# seed random number generator
seed(0)
# generate some random numbers
print(random(), random(), random())
# reset the seed
seed(0)
# generate some random numbers
print(random(), random(), random())
</pre>