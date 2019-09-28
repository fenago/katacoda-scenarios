<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# Example of training weights

# Make a prediction with weights
def predict(row, weights):
	activation = weights[0]
	for i in range(len(row)-1):
		activation += weights[i + 1] * row[i]
	return 1.0 if activation >= 0.0 else 0.0

# Estimate Perceptron weights using stochastic gradient descent
def train_weights(train, l_rate, n_epoch):
	weights = [0.0 for i in range(len(train[0]))]
	for epoch in range(n_epoch):
		sum_error = 0.0
		for row in train:
			prediction = predict(row, weights)
			error = row[-1] - prediction
			sum_error += error**2
			weights[0] = weights[0] + l_rate * error
			for i in range(len(row)-1):
				weights[i + 1] = weights[i + 1] + l_rate * error * row[i]
		print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
	return weights

# Calculate weights
dataset = [[3.7810836,6.550537003,0],
	[2.465489372,4.362125076,0],
	[4.396561688,8.400293529,0],
	[2.38807019,2.850220317,0],
	[4.06407232,6.005305973,0],
	[6.627531214,4.759262235,1],
	[4.332441248,4.088626775,1],
	[5.922596716,2.77106367,1],
	[7.675418651,-1.242068655,1],
	[6.673756466,6.508563011,1]]
l_rate = 0.2
n_epoch = 7
weights = train_weights(dataset, l_rate, n_epoch)
print(weights)

</pre>
