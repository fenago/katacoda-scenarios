<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 4
from random import seed
from random import randint
from math import ceil
from math import log10

# generate lists of random integers and their sum
def random_sum_pairs(n_examples, n_numbers, largest):
	X, y = list(), list()
	for _ in range(n_examples):
		in_pattern = [randint(1,largest) for _ in range(n_numbers)]
		out_pattern = sum(in_pattern)
		X.append(in_pattern)
		y.append(out_pattern)
	return X, y

# convert data to strings
def to_string(X, y, n_numbers, largest):
	max_length = int(n_numbers * ceil(log10(largest+1)) + n_numbers - 1)
	Xstr = list()
	for pattern in X:
		strp = '+'.join([str(n) for n in pattern])
		strp = ''.join([' ' for _ in range(max_length-len(strp))]) + strp
		Xstr.append(strp)
	max_length = int(ceil(log10(n_numbers * (largest+1))))
	ystr = list()
	for pattern in y:
		strp = str(pattern)
		strp = ''.join([' ' for _ in range(max_length-len(strp))]) + strp
		ystr.append(strp)
	return Xstr, ystr

# integer encode strings
def integer_encode(X, y, alphabet):
	char_to_int = dict((c, i) for i, c in enumerate(alphabet))
	Xenc = list()
	for pattern in X:
		integer_encoded = [char_to_int[char] for char in pattern]
		Xenc.append(integer_encoded)
	yenc = list()
	for pattern in y:
		integer_encoded = [char_to_int[char] for char in pattern]
		yenc.append(integer_encoded)
	return Xenc, yenc

seed(0)
n_samples = 2
n_numbers = 3
largest = 20
# generate pairs
X, y = random_sum_pairs(n_samples, n_numbers, largest)
print(X, y)
# convert to strings
X, y = to_string(X, y, n_numbers, largest)
print(X, y)
# integer encode
alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', ' ']
X, y = integer_encode(X, y, alphabet)
print(X, y)

</pre>

