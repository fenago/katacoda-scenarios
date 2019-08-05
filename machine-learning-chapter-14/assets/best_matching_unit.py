# Example of getting the BMU
from math import sqrt


# %%
'''
## Best Matching Unit
The Best Matching Unit or BMU is the codebook vector that is most similar to a new piece of
data. To locate the BMU for a new piece of data within a dataset we must first calculate the
distance between each codebook to the new piece of data. We can do this using our distance
function above. Once distances are calculated, we must sort all of the codebooks by their
distance to the new data. We can then return the first or most similar codebook vector. <br />

We can do this by keeping track of the distance for each record in the dataset as a tuple,
sort the list of tuples by the distance (in descending order) and then retrieve the BMU. Below
is a function named **get_best_matching_unit()** that implements this.
'''


# %%
'''
Below function nemed euclidean_distance() developed in the previous step is used
to calculate the distance between each codebook and the new test row. 
'''

# %%
# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += (row1[i] - row2[i])**2
	return sqrt(distance)


# Locate the best matching unit
def get_best_matching_unit(codebooks, test_row):
	distances = list()
	for codebook in codebooks:
		dist = euclidean_distance(codebook, test_row)
		distances.append((codebook, dist))
	distances.sort(key=lambda tup: tup[1])
	return distances[0][0]



# %%
'''
Running this example prints the BMU in the dataset to the first record. As expected, the
first record is the most similar to itself and is at the top of the list.
'''


# %%
# Test best matching unit function
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
test_row = dataset[0]
bmu = get_best_matching_unit(dataset, test_row)
print(bmu)