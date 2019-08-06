# Example of backpropagating error


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
Let's test out the backward-propagate of our network.. We define a fixed neural network
with output values and backpropagate an expected output pattern. The complete example is
listed below.

'''

# %%
# test backpropagation of error
network = [[{'output': 0.7105668883115941, 'weights': [0.13436424411240122, 0.8474337369372327, 0.763774618976614]}],
		[{'output': 0.6213859615555266, 'weights': [0.2550690257394217, 0.49543508709194095]}, {'output': 0.6573693455986976, 'weights': [0.4494910647887381, 0.651592972722763]}]]
expected = [0, 1]
backward_propagate_error(network, expected)
for layer in network:
	print(layer)


# %%
'''
Running the above example prints the network after the backpropagation of error is complete. You
can see that error values are calculated and stored in the neurons for the output layer and the
hidden layer.
'''