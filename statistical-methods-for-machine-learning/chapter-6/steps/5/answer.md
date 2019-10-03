<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab
# generate random Gaussian values
from random import seed
from random import gauss
# seed random number generator
seed(0)
# generate some Gaussian values
for _ in range(5):
	value = gauss(5, 10)
	print(value)

</pre>

