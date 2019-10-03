<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 4
# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(0)
# generate some integers
for _ in range(5):
	value = randint(5, 50)
	print(value)
</pre>

