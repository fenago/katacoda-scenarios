# %%
'''
## Normalize Data
Normalization can refer to different techniques depending on context. Here, we use normalization
to refer to rescaling an input variable to the range between 0 and 1. Normalization requires
that you know the minimum and maximum values for each attribute.

You can easily estimate the minimum and maximum values for each
attribute in a dataset by enumerating through the values. The snippet of code below defines
the dataset minmax() function that calculates the min and max value for each attribute in a
dataset, then returns an array of these minimum and maximum values.
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
With this contrived dataset, we can test our function for calculating the min and max for
each column.
'''

# %%
# Contrive small dataset
dataset = [[50, 30], [20, 90]]
print(dataset)
# Calculate min and max for each column
minmax = dataset_minmax(dataset)
print(minmax)