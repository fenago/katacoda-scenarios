<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# Example of making predictions

# Make a prediction with weights
def predict(row, weights):
	activation = weights[0]
	for i in range(len(row)-1):
		activation += weights[i + 1] * row[i]
	return 1.0 if activation >= 0.0 else 0.0

# test predictions
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
weights = [-0.1, 0.20653640140000007, -0.23418117710000003]
for row in dataset:
	prediction = predict(row, weights)
	print("Expected=%d, Predicted=%d" % (row[-1], prediction))

</pre>