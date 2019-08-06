# %%
# Example of getting neighbours for an instance
from math import sqrt


# %%
'''
## Get Neighbors
Neighbors for a new piece of data in the dataset are the k closest instances, as defined by our
distance measure. To locate the neighbors for a new piece of data within a dataset we must
first calculate the distance between each record in the dataset to the new piece of data. We can
do this using our distance function above. Once distances are calculated, we must sort all of the
records in the training dataset by their distance to the new data. We can then select the top k
to return as the most similar neighbors.<br />

We can do this by keeping track of the distance for each record in the dataset as a tuple,
sort the list of tuples by the distance (in descending order) and then retrieve the neighbors.
Below is a function named get neighbors() that implements this.
'''


# %%
# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += (row1[i] - row2[i])**2
	return sqrt(distance)


# %%
'''
You can see that the euclidean distance() function is used
to calculate the distance between each train row and the new test row. The list of train row
and distance tuples is sorted where a custom key is used ensuring that the second item in the
tuple (tup[1]) is used in the sorting operation.
Finally, a list of the num neighbors most similar neighbors to test row is returned. 
'''

# %%
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


# %%
'''
Running the following example prints the 3 most similar records in the dataset to the first record, in
order of similarity. As expected, the first record is the most similar to itself and is at the top of
the list.
'''

# %%
# Test distance function
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
neighbors = get_neighbors(dataset, dataset[0], 3)
for neighbor in neighbors:
	print(neighbor)