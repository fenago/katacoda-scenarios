# %%
'''
## Normalize Data
Normalization can refer to different techniques depending on context. Here, we use normalization
to refer to rescaling an input variable to the range between 0 and 1. Normalization requires
that you know the minimum and maximum values for each attribute.
'''

# %%
# Find the min and max values for each column
def dataset_minmax(dataset):
	minmax = list()
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		value_min = min(col_values)
		value_max = max(col_values)
		minmax.append([value_min, value_max])
	return minmax

# %%
'''
Below is an implementation of this in a function called normalize dataset() that normalizes
values in each column of a provided dataset.
'''

# %%
# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset, minmax):
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

# %%
'''
We can tie normalize_dataset function together with the dataset minmax() function and normalize the
contrived dataset
'''

# %%
# Contrive small dataset
dataset = [[50, 30], [20, 90]]
print(dataset)
# Calculate min and max for each column
minmax = dataset_minmax(dataset)
print(minmax)
# Normalize columns
normalize_dataset(dataset, minmax)
print(dataset)