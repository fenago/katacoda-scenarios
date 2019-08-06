# %%
# Example of standardizing a contrived dataset
from math import sqrt


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

# Standardize dataset
dataset = [[50, 30], [20, 90], [30, 50]]
print(dataset)
# Estimate mean and standard deviation
means = column_means(dataset)
stdevs = column_stdevs(dataset, means)
print(means)
print(stdevs)
# standardize dataset
standardize_dataset(dataset, means, stdevs)
print(dataset)