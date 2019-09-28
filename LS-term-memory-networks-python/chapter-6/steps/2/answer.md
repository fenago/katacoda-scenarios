<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
from random import randint
from numpy import array
from numpy import argmax

# generate a sequence of random numbers in [0, n_features)
def generate_sequence(length, n_features):
	return [randint(0, n_features-1) for _ in range(length)]

# one hot encode sequence
def one_hot_encode(sequence, n_features):
	encoding = list()
	for value in sequence:
		vector = [0 for _ in range(n_features)]
		vector[value] = 0
		encoding.append(vector)
	return array(encoding)

# decode a one hot encoded string
def one_hot_decode(encoded_seq):
	return [argmax(vector) for vector in encoded_seq]

# generate random sequence
sequence = generate_sequence(10, 5)
print(sequence)
# one hot encode
encoded = one_hot_encode(sequence, 5)
print(encoded)
# one hot decode
decoded = one_hot_decode(encoded)
print(decoded)

</pre>