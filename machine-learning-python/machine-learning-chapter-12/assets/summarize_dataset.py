# %%
# Example of summarizing a dataset
from math import sqrt


# %%
'''
## Summarize Dataset
We need two statistics from a given set of data. We'll see how these statistics are used in the
calculation of probabilities in a few steps. The two statistics we require from a given dataset
are the mean and the standard deviation (average deviation from the mean). The mean is the average value 
'''

# %%
# Calculate the mean of a list of numbers
def mean(numbers):
	return sum(numbers)/float(len(numbers))


# %%
'''
Sample standard deviation is calculated as the mean difference from the mean value. Below is a function named stdev() calculates 
standard deviation.
'''

# %%
# Calculate the standard deviation of a list of numbers
def stdev(numbers):
	avg = mean(numbers)
	variance = sum([(x-avg)**2 for x in numbers]) / float(len(numbers)-1)
	return sqrt(variance)


# %%
'''
We require the mean and standard deviation statistics to be calculated for each input
attribute or each column of our data. We can do that by gathering all of the values for each
column into a list and calculating the mean and standard deviation on that list. Once calculated,
we can gather the statistics together into a list or tuple of statistics. Then, repeat this operation
for each column in the dataset and return a list of tuples of statistics.
Below is a function named summarize_dataset() that implements this approach.
'''

# %%
# Calculate the mean, stdev and count for each column in a dataset
def summarize_dataset(dataset):
	summaries = [(mean(column), stdev(column), len(column)) for column in zip(*dataset)]
	del(summaries[-1])
	return summaries


# %%
'''
Running the following example prints out the list of tuples of statistics on each of the two input
variables. Interpreting the results, we can see that the mean value of X1 is 5.178333386499999
and the standard deviation of X1 is 2.7665845055177263.
'''

# %%
# Test summarizing a dataset
dataset = [[3.393533211,2.331273381,0],
	[3.110073483,1.781539638,0],
	[1.343808831,3.368360954,0],
	[3.582294042,4.67917911,0],
	[2.280362439,2.866990263,0],
	[7.423436942,4.696522875,1],
	[5.745051997,3.533989803,1],
	[9.172168622,2.511101045,1],
	[7.792783481,3.424088941,1],
	[7.939820817,0.791637231,1]]
summary = summarize_dataset(dataset)
print(summary)