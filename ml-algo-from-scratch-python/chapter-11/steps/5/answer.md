<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 5
# Example of making predictions

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

# contrived dataset
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
#  predict with a stump
stump = {'index': 0, 'right': 1, 'value': 6.642287351, 'left': 0}
for row in dataset:
	prediction = predict(stump, row)
	print('Expected=%d, Got=%d' % (row[-1], prediction))
</pre>

