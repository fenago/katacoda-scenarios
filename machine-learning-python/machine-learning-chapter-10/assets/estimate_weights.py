# %%
'''
## Making Predictions
The first step is to develop a function that can make predictions. This will be needed both in
the evaluation of candidate weight values in stochastic gradient descent, and after the model is
finalized and we wish to start making predictions on test data or new data. Below is a function
named predict() that predicts an output value for a row given a set of weights. The first
weight is always the bias as it is standalone and not responsible for a specific input value.
'''

# %%
# Make a prediction with weights
def predict(row, weights):
	activation = weights[0]
	for i in range(len(row)-1):
		activation += weights[i + 1] * row[i]
	return 1.0 if activation >= 0.0 else 0.0



# %%
'''
## Training Network Weights
We can estimate the weight values for our training data using stochastic gradient descent.
Stochastic gradient descent requires two parameters:
- **Learning Rate:**: Used to limit the amount each weight is corrected each time it is
updated.
- **Epochs:** The number of times to run through the training data while updating the weight.
These, along with the training data will be the arguments to the function. There are 3 loops
we need to perform in the function:
'''


# %%
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

# %%
'''
We will use a learning rate of 0.1 and train the model for only 5 epochs, or 5 exposures of the
weights to the entire training dataset. Running the example below prints a message each epoch with
the sum squared error for that epoch and the final set of weights.
'''


# %%
# Calculate weights
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
l_rate = 0.1
n_epoch = 5
weights = train_weights(dataset, l_rate, n_epoch)
print(weights)


# %%
'''
You can see how the problem is learned very quickly by the algorithm.
'''