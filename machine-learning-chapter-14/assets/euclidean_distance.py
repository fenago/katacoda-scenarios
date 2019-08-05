# %%
# Example of calculating Euclidean distance
from math import sqrt

# %%
'''
## Euclidean Distance
The first step needed is to calculate the distance between two rows in a dataset. Rows of data
are mostly made up of numbers and an easy way to calculate the distance between two rows or
vectors of numbers is to draw a straight line. This makes sense in 2D or 3D and scales nicely
to higher dimensions. We can calculate the straight line distance between two vectors using
the Euclidean distance measure. It is calculated as the square root of the sum of the squared
differences between the two vectors.<br />

Where x1 is the first row of data, x2 is the second row of data and i is the index to a specific
column as we sum across all columns. With Euclidean distance, the smaller the value, the more
similar two records will be. A value of 0 means that there is no difference between two records.
Below is a function named euclidean distance() that implements this in Python.
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
Let's test a small example to test our distance function by printing the distance between the first row and all other rows. We would expect the 
distance between the first row and itself to be 0, a good thing to look out for.<br />

Running this example prints the distances between the first row and every row in the dataset,
including itself
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
row0 = dataset[0]
for row in dataset:
	distance = euclidean_distance(row0, row)
	print(distance)