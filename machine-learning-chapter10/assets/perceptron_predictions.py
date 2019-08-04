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
There are two inputs values (X1 and X2) and three weight values (bias, w1 and w2). The
activation equation we have modeled for this problem is:<br />
activation = (w1 × X1) + (w2 × X2) + bias (10.4)<br />
Or, with the specific weight values we chose by hand as:<br />
activation = (0:206 × X1) + (−0:234 × X2) + −0:1 (10.5)<br />
Running this function we get predictions that match the expected output (y) values.
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
weights = [-0.1, 0.20653640140000007, -0.23418117710000003]
for row in dataset:
	prediction = predict(row, weights)
	print("Expected=%d, Predicted=%d" % (row[-1], prediction))