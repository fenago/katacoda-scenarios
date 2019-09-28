<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab in Step 3
# Example of forward propagating input
from math import exp

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

# test forward propagation
network = [{'weights': [0.8444218515250481, 0.7579544029403025]}, {'weights': [0.420571580830845, 0.25891675029296335]}],
[{'weights': [0.5112747213686085, 0.4049341374504143, 0.7837985890347726]}]
row = [1, 0, None]
output = forward_propagate(network, row)
print(output)

</pre>
