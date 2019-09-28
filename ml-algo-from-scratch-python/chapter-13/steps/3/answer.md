<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# Example of getting neighbours for an instance
from math import sqrt

# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += (row1[i] - row2[i])**2
	return sqrt(distance)

# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
	distances = list()
	for train_row in train:
		dist = euclidean_distance(test_row, train_row)
		distances.append((train_row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors

# Test distance function
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
neighbors = get_neighbors(dataset, dataset[0], 3)
for neighbor in neighbors:
	print(neighbor)

</pre>
