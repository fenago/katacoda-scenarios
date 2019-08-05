# %%
# Example of normalizing the diabetes dataset
from csv import reader

# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

# %%
# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())

# %%
'''
Normalize Data
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
We can now load and normalize the Pima Indians Diabetes dataset. The example first loads the dataset and converts the values for
each column from string to floating point values. The minimum and maximum values for each
column are estimated from the dataset, and finally, the values in the dataset are normalized
'''

# %%
# Load pima-indians-diabetes dataset
filename = 'pima-indians-diabetes.csv'
dataset = load_csv(filename)
print('Loaded data file {0} with {1} rows and {2} columns'.format(filename, len(dataset), len(dataset[0])))
# convert string columns to float
for i in range(len(dataset[0])):
	str_column_to_float(dataset, i)
print(dataset[0])
# Calculate min and max for each column
minmax = dataset_minmax(dataset)
# Normalize columns
normalize_dataset(dataset, minmax)
print(dataset[0])