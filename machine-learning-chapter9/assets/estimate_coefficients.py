# %%
# Example of estimating coefficients
from math import exp


# %%
'''
## Logistic Regression
Logistic regression is named for the function used at the core of the method, the logistic function.
Logistic regression uses an equation as the representation, very much like linear regression.
Input values (X) are combined linearly using weights or coefficient values to predict an output
value (y). A key difference from linear regression is that the output value being modeled is a
binary value (0 or 1) rather than a numeric value.
'''


# %%
# Make a prediction with coefficients
def predict(row, coefficients):
	yhat = coefficients[0]
	for i in range(len(row)-1):
		yhat += coefficients[i + 1] * row[i]
	return 1.0 / (1.0 + exp(-yhat))


# %%
'''
## Estimating Coefficients
We can estimate the coefficient values for our training data using stochastic gradient descent.
Stochastic gradient descent requires two parameters:
- **Learning Rate:** Used to limit the amount each coefficient is corrected each time it is
updated.
- **Epochs:** The number of times to run through the training data while updating the
coefficients.
'''

# %%
# Estimate logistic regression coefficients using stochastic gradient descent
def coefficients_sgd(train, l_rate, n_epoch):
	coef = [0.0 for i in range(len(train[0]))]
	for epoch in range(n_epoch):
		sum_error = 0
		for row in train:
			yhat = predict(row, coef)
			error = row[-1] - yhat
			sum_error += error**2
			coef[0] = coef[0] + l_rate * error * yhat * (1.0 - yhat)
			for i in range(len(row)-1):
				coef[i + 1] = coef[i + 1] + l_rate * error * yhat * (1.0 - yhat) * row[i]
		print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
	return coef


# %%
'''
We will use a larger learning rate of 0.3 and train the model for 100 epochs, or 100 exposures
of the coefficients to the entire training dataset. Running the example prints a message each
epoch with the sum squared error for that epoch and the final set of coefficients.
'''

# %%
# Calculate coefficients
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
l_rate = 0.3
n_epoch = 100
coef = coefficients_sgd(dataset, l_rate, n_epoch)
print(coef)


# %%
'''
You can see how error continues to drop even in the final epoch. We could probably train for
a lot longer (more epochs) or increase the amount we update the coefficients each epoch (higher
learning rate).
'''