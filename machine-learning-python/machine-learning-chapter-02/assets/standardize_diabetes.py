# %%
# Standardize the Diabetes Dataset
from csv import reader
from math import sqrt

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

# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())


# %%
'''
## Standardize Data
Standardization is a rescaling technique that refers to centering the distribution of the data on
the value 0 and the standard deviation to the value 1. Together, the mean and the standard
deviation can be used to summarize a normal distribution, also called the Gaussian distribution
or bell curve.
'''

# %%
'''
Let's start with creating functions to estimate the mean and standard deviation statistics for each column from a dataset. The mean describes
the middle or central tendency for a collection of numbers. The mean for a column is calculated
as the sum of all values for a column divided by the total number of values.

The function below named column means() calculates the mean values for each column in
the dataset
'''

# %%
# calculate column means
def column_means(dataset):
	means = [0 for i in range(len(dataset[0]))]
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		means[i] = sum(col_values) / float(len(dataset))
	return means

# %%
'''
The function below named column stdevs() calculates the standard deviation of values for
each column in the dataset and assumes the means have already been calculated
'''

# %%
# calculate column standard deviations
def column_stdevs(dataset, means):
	stdevs = [0 for i in range(len(dataset[0]))]
	for i in range(len(dataset[0])):
		variance = [pow(row[i]-means[i], 2) for row in dataset]
		stdevs[i] = sum(variance)
	stdevs = [sqrt(x/(float(len(dataset)-1))) for x in stdevs]
	return stdevs


# %%
'''
Once the summary statistics are calculated, we can easily standardize the values in each
column. The calculation to standardize a given value is as follows:
Below is a function named standardize dataset() that implements this equation
'''

# %%
# standardize dataset
def standardize_dataset(dataset, means, stdevs):
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - means[i]) / stdevs[i]


# %%
'''
Running the example prints the first row of the dataset, first in a raw format as loaded, and
then standardized which allows us to see the difference for comparison.
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
# Estimate mean and standard deviation
means = column_means(dataset)
stdevs = column_stdevs(dataset, means)
# standardize dataset
standardize_dataset(dataset, means, stdevs)
print(dataset[0])