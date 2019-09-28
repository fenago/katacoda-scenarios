<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab in Step 3
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

# generate one example for an lstm
def generate_example(length, n_features, out_index):
	# generate sequence
	sequence = generate_sequence(length, n_features)
	# one hot encode
	encoded = one_hot_encode(sequence, n_features)
	# reshape sequence to be 3D
	X = encoded.reshape((1, length, n_features))
	# select output
	y = encoded[out_index].reshape(1, n_features)
	return X, y

X, y = generate_example(5, 10, 1)
print(X.shape)
print(y.shape)

</pre>
