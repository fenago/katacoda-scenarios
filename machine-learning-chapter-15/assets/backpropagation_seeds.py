# %%
# Backprop on the Seeds Dataset
from random import seed
from random import randrange
from random import random
from csv import reader
from math import exp

# %%
'''
## Wheat Seeds Case Study
This section applies the Backpropagation algorithm to the wheat seeds dataset. 

Input values vary in scale and need to be normalized to the range of 0 and 1. It is generally
good practice to normalize input values to the range of the chosen transfer function, in this
case, the sigmoid function that outputs values between 0 and 1. The dataset minmax() and
normalize dataset() helper functions were used to normalize the input values.
'''

# %%
'''
The first step is to load the dataset and convert the loaded data to numbers that we can use in our neural network.
For this we will use the helper function load csv() to load the file, str column to float()
to convert string numbers to floats and str column to int() to convert the class column to
integer values.
'''

# %%
# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())

# Convert string column to integer
def str_column_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup

# Find the min and max values for each column
def dataset_minmax(dataset):
	return [[min(column), max(column)] for column in zip(*dataset)]

# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset, minmax):
	for row in dataset:
		for i in range(len(row)-1):
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])


# %%
'''
We will evaluate the algorithm using k-fold cross-validation with 5 folds. This means that
201/5 = 40.2 or 40 records will be in each fold. We will use the helper functions evaluate algorithm()
to evaluate the algorithm with cross-validation and accuracy metric() to calculate the accuracy
of predictions.
A new function named back propagation() was developed to manage the application of the
Backpropagation algorithm, first initializing a network, training it on the training dataset and
then using the trained network to make predictions on a test dataset. The complete example is
listed below.
'''

# %%
# Split a dataset into k folds
def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	for _ in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split

# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0

# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
	folds = cross_validation_split(dataset, n_folds)
	scores = list()
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = list()
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None
		predicted = algorithm(train_set, test_set, *args)
		actual = [row[-1] for row in fold]
		accuracy = accuracy_metric(actual, predicted)
		scores.append(accuracy)
	return scores

# %%
'''
## Forward-Propagate
We can calculate an output from a neural network by propagating an input signal through
each layer until the output layer outputs its values. We call this forward-propagation. It is the
technique we will need to generate predictions during training that will need to be corrected,
and it is the method we will need after the network is trained to make predictions on new data.

We can break forward-propagation down into three parts:
1. Neuron Activation.
2. Neuron Transfer.
3. Forward-Propagation.
'''

# %%
# Calculate neuron activation for an input
def activate(weights, inputs):
	activation = weights[-1]
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]
	return activation

# Transfer neuron activation
def transfer(activation):
	return 1.0 / (1.0 + exp(-activation))

# Forward propagate input to a network output
def forward_propagate(network, row):
	inputs = row
	for layer in network:
		new_inputs = []
		for neuron in layer:
			activation = activate(neuron['weights'], inputs)
			neuron['output'] = transfer(activation)
			new_inputs.append(neuron['output'])
		inputs = new_inputs
	return inputs


# %%
'''
## Backpropagate Error
The backpropagation algorithm is named for the way in which weights are trained. Error is
calculated between the expected outputs and the outputs forward-propagated from the network.
These errors are then propagated backward through the network from the output layer to the
hidden layer, assigning blame for the error and updating weights as they go. The math for
backpropagating error is rooted in calculus, but we will remain high level in this section and
focus on what is calculated and how rather than why the calculations take this particular form.
This part is broken down into two sections.
1. Transfer Derivative.
2. Error Backpropagation.
'''

# %%
# Calculate the derivative of an neuron output
def transfer_derivative(output):
	return output * (1.0 - output)

# Backpropagate error and store in neurons
def backward_propagate_error(network, expected):
	for i in reversed(range(len(network))):
		layer = network[i]
		errors = list()
		if i != len(network)-1:
			for j in range(len(layer)):
				error = 0.0
				for neuron in network[i + 1]:
					error += (neuron['weights'][j] * neuron['delta'])
				errors.append(error)
		else:
			for j in range(len(layer)):
				neuron = layer[j]
				errors.append(expected[j] - neuron['output'])
		for j in range(len(layer)):
			neuron = layer[j]
			neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])

# Update network weights with error
def update_weights(network, row, l_rate):
	for i in range(len(network)):
		inputs = row[:-1]
		if i != 0:
			inputs = [neuron['output'] for neuron in network[i - 1]]
		for neuron in network[i]:
			for j in range(len(inputs)):
				neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
			neuron['weights'][-1] += l_rate * neuron['delta']

# Train a network for a fixed number of epochs
def train_network(network, train, l_rate, n_epoch, n_outputs):
	for _ in range(n_epoch):
		for row in train:
			forward_propagate(network, row)
			expected = [0 for i in range(n_outputs)]
			expected[row[-1]] = 1
			backward_propagate_error(network, expected)
			update_weights(network, row, l_rate)

# Initialize a network
def initialize_network(n_inputs, n_hidden, n_outputs):
	network = list()
	hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
	network.append(hidden_layer)
	output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
	network.append(output_layer)
	return network

# Make a prediction with a network
def predict(network, row):
	outputs = forward_propagate(network, row)
	return outputs.index(max(outputs))

# %%
'''
A new function named back_propagation() was developed to manage the application of the
Backpropagation algorithm, first initializing a network, training it on the training dataset and
then using the trained network to make predictions on a test dataset. The complete example is
listed below.
'''

# %%
# Backpropagation Algorithm With Stochastic Gradient Descent
def back_propagation(train, test, l_rate, n_epoch, n_hidden):
	n_inputs = len(train[0]) - 1
	n_outputs = len(set([row[-1] for row in train]))
	network = initialize_network(n_inputs, n_hidden, n_outputs)
	train_network(network, train, l_rate, n_epoch, n_outputs)
	predictions = list()
	for row in test:
		prediction = predict(network, row)
		predictions.append(prediction)
	return(predictions)


# %%
# Test Backprop on Seeds dataset
seed(1)
# load and prepare data
filename = 'seeds_dataset.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])-1):
	str_column_to_float(dataset, i)
# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)
# normalize input variables
minmax = dataset_minmax(dataset)
normalize_dataset(dataset, minmax)
# evaluate algorithm
n_folds = 5
l_rate = 0.3
n_epoch = 500
n_hidden = 5
scores = evaluate_algorithm(dataset, back_propagation, n_folds, l_rate, n_epoch, n_hidden)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))


# %%
'''
A network with 5 neurons in the hidden layer and 3 neurons in the output layer was
constructed. The network was trained for 500 epochs with a learning rate of 0.3. These
parameters were found with a little trial and error, but you may be able to do much better.
Running the example prints the average classification accuracy on each fold as well as the
average performance across all folds.

You can see that backpropagation and the chosen configuration achieved a mean classification
accuracy which is dramatically better than the baseline of 28% accuracy.
'''