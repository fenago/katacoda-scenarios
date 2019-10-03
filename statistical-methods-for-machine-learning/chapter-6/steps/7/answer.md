<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 7
# select a random sample without replacement
from random import seed
from random import sample
# seed random number generator
seed(0)
# prepare a sequence
sequence = [i for i in range(10)]
print(sequence)
# select a subset without replacement
subset = sample(sequence, 10)
print(subset)

</pre>

