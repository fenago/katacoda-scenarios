# %%
# Example of initializing a network
from random import seed
from random import random


# %%
'''
## Initialize Network
Below is a function named initialize_network() that creates a new neural network ready
for training. It accepts three parameters: the number of inputs, the number of neurons to have
in the hidden layer and the number of outputs. You can see that for the hidden layer we create
n hidden neurons and each neuron in the hidden layer has n inputs + 1 weights, one for each
input column in a dataset and an additional one for the bias.

You can also see that the output layer that connects to the hidden layer has n outputs
neurons, each with n hidden + 1 weights. This means that each neuron in the output layer
connects to (has a weight for) each neuron in the hidden layer
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
Let's test out above function. Below is a complete example that creates a small network.<br />

Running the example, you can see that the code prints out each layer one by one. You can
see the hidden layer has one neuron with 2 input weights plus the bias. The output layer has 2
neurons, each with 1 weight plus the bias.
'''

# %%
# Test initializing a network
seed(1)
network = initialize_network(2, 1, 2)
for layer in network:
	print(layer)