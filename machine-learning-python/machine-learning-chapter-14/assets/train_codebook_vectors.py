# %%
# Example of training a set of codebook vectors
from math import sqrt
from random import randrange
from random import seed


# %%
'''
## Training Codebook Vectors
The first step in training a set of codebook vectors is to initialize the set. We can initialize it with
patterns constructed from random features in the training dataset. Below is a function named
random codebook() that implements this. Random input and output features are selected from
the training data.

After the codebook vectors are initialized to a random set, they must be adapted to best summarize the training data. 
This is done iteratively.

- **Epochs:** At the top level, the process is repeated for a fixed number of epochs or exposures
of the training data.
- **Training Dataset:** Within an epoch, each training pattern is used one at a time to
update the set of codebook vectors.
- **Pattern Features:** For a given training pattern, each feature of a best matching codebook
vector is updated to move it closer or further away.
'''


# %%
# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += (row1[i] - row2[i])**2
	return sqrt(distance)

# Locate the best matching unit
def get_best_matching_unit(codebooks, test_row):
	distances = list()
	for codebook in codebooks:
		dist = euclidean_distance(codebook, test_row)
		distances.append((codebook, dist))
	distances.sort(key=lambda tup: tup[1])
	return distances[0][0]

# Create a random codebook vector
def random_codebook(train):
	n_records = len(train)
	n_features = len(train[0])
	codebook = [train[randrange(n_records)][i] for i in range(n_features)]
	return codebook


# %%
'''
Below is a function named train codebooks()
implements the procedure for training a set of codebook vectors given a training dataset. The
function takes 3 additional arguments to the training dataset, the number of codebook vectors
to create and train, the initial learning rate and the number of epochs for which to train the
codebook vectors.
'''

# %%
# Train a set of codebook vectors
def train_codebooks(train, n_codebooks, lrate, epochs):
	codebooks = [random_codebook(train) for i in range(n_codebooks)]
	for epoch in range(epochs):
		rate = lrate * (1.0-(epoch/float(epochs)))
		sum_error = 0.0
		for row in train:
			bmu = get_best_matching_unit(codebooks, row)
			for i in range(len(row)-1):
				error = row[i] - bmu[i]
				sum_error += error**2
				if bmu[-1] == row[-1]:
					bmu[i] += rate * error
				else:
					bmu[i] -= rate * error
		print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, rate, sum_error))
	return codebooks


# %%
'''
Running this example trains a set of 2 codebook vectors for 10 epochs with an initial learning
rate of 0.3. The details are printed each epoch and the set of 2 codebook vectors learned
from the training data is displayed. We can see that the changes to learning rate meet our
expectations explored above for each epoch. We can also see that the sum squared error each
epoch does continue to drop at the end of training and that there may be an opportunity to
tune the example further to achieve less error.
'''

# %%
# Test the training function
seed(1)
dataset = [[2.7810836,2.550537003,0],
	[1.465489372,2.362125076,0],
	[3.396561688,4.400293529,0],
	[1.38807019,1.850220317,0],
	[3.06407232,3.005305973,0],
	[7.627531214,2.759262235,1],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1],
	[8.675418651,-0.242068655,1],
	[7.673756466,3.508563011,1]]
learn_rate = 0.3
n_epochs = 10
n_codebooks = 2
codebooks = train_codebooks(dataset, n_codebooks, learn_rate, n_epochs)
print('Codebooks: %s' % codebooks)