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
# Example of making a prediction
from math import exp


# %%
'''
## Making Predictions
The first step is to develop a function that can make predictions. This will be needed both
in the evaluation of candidate coefficient values in stochastic gradient descent and after the
model is finalized and we wish to start making predictions on test data or new data. Below is a
function named predict() that predicts an output value for a row given a set of coefficients.
The first coefficient in is always the intercept, also called the bias or b0 as it is standalone and
not responsible for a specific input value.
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
There are two inputs values (X1 and X2) and three coefficient values (b0, b1 and b2).
Running the following snippet will give predictions that are reasonably close to the expected output
(y) values and when rounded make correct predictions of the class.
'''


# %%
# test predictions
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
coef = [-0.406605464, 0.852573316, -1.104746259]
for row in dataset:
	yhat = predict(row, coef)
	print("Expected=%.3f, Predicted=%.3f [%d]" % (row[-1], yhat, round(yhat)))