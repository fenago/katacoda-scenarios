<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# generate random dice rolls
from numpy.random import seed
from numpy.random import randint
from numpy import mean
# seed the random number generator
seed(0)
# generate a sample of die rolls
rolls = randint(2, 5, 20)
print(rolls)
print(mean(rolls))
</pre>