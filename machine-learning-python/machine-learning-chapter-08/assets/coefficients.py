# %%
'''
## Estimating Coefficients
We can estimate the coefficient values for our training data using stochastic gradient descent.
Stochastic gradient descent requires two parameters:<br />
- **Learning Rate:** Used to limit the amount that each coefficient is corrected each time it
is updated.
- **Epochs:** The number of times to run through the training data while updating the
coefficients.
'''

# %%
# Make a prediction
def predict(row, coefficients):
	yhat = coefficients[0]
	for i in range(len(row)-1):
		yhat += coefficients[i + 1] * row[i]
	return yhat



# %%
'''
Below is a function named coefficients sgd() that calculates coefficient values for a training dataset
using stochastic gradient descent.
'''

# %%
# Estimate linear regression coefficients using stochastic gradient descent
def coefficients_sgd(train, l_rate, n_epoch):
	coef = [0.0 for i in range(len(train[0]))]
	for epoch in range(n_epoch):
		sum_error = 0
		for row in train:
			yhat = predict(row, coef)
			error = yhat - row[-1]
			sum_error += error**2
			coef[0] = coef[0] - l_rate * error
			for i in range(len(row)-1):
				coef[i + 1] = coef[i + 1] - l_rate * error * row[i]
		print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
	return coef


# %%
'''
We will use a small learning rate of 0.001 and train the model for 50 epochs, or 50 exposures
of the coefficients to the entire training dataset. Running the example below prints a message each
epoch with the sum squared error for that epoch and the final set of coefficients.
'''

# %%
# Calculate coefficients
dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
l_rate = 0.001
n_epoch = 50
coef = coefficients_sgd(dataset, l_rate, n_epoch)
print(coef)


# %%
'''
You can see how error continues to drop even in the final epoch. We could probably train for
a lot longer (more epochs) or increase the amount we update the coefficients each epoch (higher
learning rate).
'''