# %%
# Example of training a network by backpropagation
from math import exp
from random import seed
from random import random


# %%
'''
## Train Network
The network is trained using stochastic gradient descent. The procedure involves multiple iterations of exposing a training
dataset to the network and for each row of data forward-propagating the inputs, backpropagating
the error and updating the network weights. This part is broken down into two sections:
1. Update Weights.
2. Train Network
'''

# %%
# Initialize a network
def initialize_network(n_inputs, n_hidden, n_outputs):
	network = list()
	hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
	network.append(hidden_layer)
	output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
	network.append(output_layer)
	return network


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


# %%
'''
Train Network is broken down into two sections:
1. Update Weights.
2. Train Network
'''

# %%
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
	for epoch in range(n_epoch):
		sum_error = 0
		for row in train:
			outputs = forward_propagate(network, row)
			expected = [0 for i in range(n_outputs)]
			expected[row[-1]] = 1
			sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
			backward_propagate_error(network, expected)
			update_weights(network, row, l_rate)
		print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))


# %%
'''
We now have all of the pieces to train the network. We can put together an example that
includes everything we've seen so far including network initialization and train a network on
a small dataset. Below is a small contrived dataset that we can use to test out training our
neural network
'''

# %%
# Test training backprop algorithm
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
n_inputs = len(dataset[0]) - 1
n_outputs = len(set([row[-1] for row in dataset]))
network = initialize_network(n_inputs, 2, n_outputs)
train_network(network, dataset, 0.5, 20, n_outputs)
for layer in network:
	print(layer)


# %%
'''
Running the example first prints the sum squared error each training epoch. We can see a
trend of this error decreasing with each epoch. Once trained, the network is printed, showing
the learned weights. Also still in the network are output and delta values that can be ignored.
We could update our training function to delete these data if we wanted.
'''