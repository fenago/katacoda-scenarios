# %%
'''
## Making Predictions
The first step is to develop a function that can make predictions. This will be needed both
in the evaluation of candidate coefficient values in stochastic gradient descent and after the
model is finalized and we wish to start making predictions on test data or new data. <br />
Below is a function named predict() that predicts an output value for a row given a set of coefficients.
The first coefficient in is always the intercept, also called the bias or b0 as it is standalone and
not responsible for a specific input value.
'''

# %%
# Make a prediction
def predict(row, coefficients):
	yhat = coefficients[0]
	for i in range(len(row)-1):
		yhat += coefficients[i + 1] * row[i]
	return yhat

dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
coef = [0.4, 0.8]
for row in dataset:
	yhat = predict(row, coef)
	print("Expected=%.3f, Predicted=%.3f" % (row[-1], yhat))