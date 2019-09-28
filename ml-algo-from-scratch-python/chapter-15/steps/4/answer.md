<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 4
# Example of backpropagating error

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

# test backpropagation of error
network = [[{'output': 0.8105668883115941, 'weights': [0.8444218515250481, 0.7579544029403025]}],
		[{'output': 0.7213859615555266, 'weights': [0.420571580830845, 0.25891675029296335]}, {'output': 0.8573693455986976, 'weights': [0.5112747213686085, 0.4049341374504143, 0.7837985890347726]}]]
expected = [0, 1]
backward_propagate_error(network, expected)
for layer in network:
	print(layer)
</pre>

