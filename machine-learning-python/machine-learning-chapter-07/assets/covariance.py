# %%
'''
Below is a function named mean() that calculates the mean for a list of numbers.
'''

# %%
# Calculate the mean value of a list of numbers
def mean(values):
	return sum(values) / float(len(values))


# %%
'''
Below is a function named covariance() that calculates the covariance for a list of numbers.
'''

# %%
# Calculate covariance between x and y
def covariance(x, mean_x, y, mean_y):
	covar = 0.0
	for i in range(len(x)):
		covar += (x[i] - mean_x) * (y[i] - mean_y)
	return covar


# %%
# Example of Calculating Covariance
dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
x = [row[0] for row in dataset]
y = [row[1] for row in dataset]
mean_x, mean_y = mean(x), mean(y)
covar = covariance(x, mean_x, y, mean_y)
print('Covariance: %.3f' % (covar))