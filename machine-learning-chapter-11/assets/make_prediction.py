# %%
'''
## Make a Prediction
Making predictions with a decision tree involves navigating the tree with the specifically provided
row of data. Again, we can implement this using a recursive function, where the same prediction
routine is called again with the left or the right child nodes, depending on how the split affects
the provided data. We must check if a child node is either a terminal value to be returned as
the prediction, or if it is a dictionary node containing another level of the tree to be considered.<br />

Below is the predict() function that implements this procedure. You can see how the index
and value in a given node is used to evaluate whether the row of provided data falls on the left
or the right of the split.
'''

# %%
# Make a prediction with a decision tree
def predict(node, row):
	if row[node['index']] < node['value']:
		if isinstance(node['left'], dict):
			return predict(node['left'], row)
		else:
			return node['left']
	else:
		if isinstance(node['right'], dict):
			return predict(node['right'], row)
		else:
			return node['right']


# %%
'''
We can use our contrived dataset to test this function. Below is an example that uses a
hard-coded decision tree with a single node that best splits the data (a decision stump). The
example makes a prediction for each row in the dataset
'''

# %%
# contrived dataset
dataset = [[2.771244718,1.784783929,0],
	[1.728571309,1.169761413,0],
	[3.678319846,2.81281357,0],
	[3.961043357,2.61995032,0],
	[2.999208922,2.209014212,0],
	[7.497545867,3.162953546,1],
	[9.00220326,3.339047188,1],
	[7.444542326,0.476683375,1],
	[10.12493903,3.234550982,1],
	[6.642287351,3.319983761,1]]
#  predict with a stump
stump = {'index': 0, 'right': 1, 'value': 6.642287351, 'left': 0}
for row in dataset:
	prediction = predict(stump, row)
	print('Expected=%d, Got=%d' % (row[-1], prediction))


# %%
'''
Running the example prints the correct prediction for each row, as expected
'''
