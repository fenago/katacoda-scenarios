# %%
# Example of forward propagating input
from math import exp


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
Let's test out the forward-propagation of our network.
We define our network inline with one hidden neuron that expects 2 input values and an output
layer with two neurons.
'''

# %%
# test forward propagation
network = [[{'weights': [0.13436424411240122, 0.8474337369372327, 0.763774618976614]}],
		[{'weights': [0.2550690257394217, 0.49543508709194095]}, {'weights': [0.4494910647887381, 0.651592972722763]}]]
row = [1, 0, None]
output = forward_propagate(network, row)
print(output)


# %%
'''
Running the above example propagates the input pattern [1, 0] and produces an output value that
is printed. Because the output layer has two neurons, we get a list of two numbers as output.
The actual output values are just nonsense for now, but next, we will start to learn how to
make the weights in the neurons more useful.
'''