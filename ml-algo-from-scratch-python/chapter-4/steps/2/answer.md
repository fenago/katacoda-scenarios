<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# Example of calculating classification accuracy

# Calculate accuracy percentage between two lists
def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0

# Test accuracy
actual = [1,0,0,1,0,0,1,0,0,0]
predicted = [1,0,1,0,1,0,1,0,1,0]
accuracy = accuracy_metric(actual, predicted)
print(accuracy)

</pre>