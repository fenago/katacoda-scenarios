<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
from random import seed
from random import randint

# generate lists of random integers and their sum
def random_sum_pairs(n_examples, n_numbers, largest):
	X, y = list(), list()
	for _ in range(n_examples):
		in_pattern = [randint(1,largest) for _ in range(n_numbers)]
		out_pattern = sum(in_pattern)
		X.append(in_pattern)
		y.append(out_pattern)
	return X, y

seed(0)
n_samples = 2
n_numbers = 5
largest = 20
# generate pairs
X, y = random_sum_pairs(n_samples, n_numbers, largest)
print(X, y)s

</pre>