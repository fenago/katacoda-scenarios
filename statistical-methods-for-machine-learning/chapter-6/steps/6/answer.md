<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 6
# choose a random element from a list
from random import seed
from random import choice
# seed random number generator
seed(0)
# prepare a sequence
sequence = [i for i in range(10)]
print(sequence)
# make choices from the sequence
for _ in range(10):
	selection = choice(sequence)
	print(selection)
</pre>

