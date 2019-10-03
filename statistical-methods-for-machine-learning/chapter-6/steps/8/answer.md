<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 7
# randomly shuffle a sequence
from random import seed
from random import shuffle
# seed random number generator
seed(0)
# prepare a sequence
sequence = [i for i in range(10)]
print(sequence)
# randomly shuffle the sequence
shuffle(sequence)
print(sequence)

</pre>

