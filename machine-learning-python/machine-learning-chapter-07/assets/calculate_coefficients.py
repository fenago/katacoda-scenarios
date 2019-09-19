# %%
# Example of Calculating Coefficients

# Calculate the mean value of a list of numbers
def mean(values):
	return sum(values) / float(len(values))

# Calculate covariance between x and y
def covariance(x, mean_x, y, mean_y):
	covar = 0.0
	for i in range(len(x)):
		covar += (x[i] - mean_x) * (y[i] - mean_y)
	return covar


# %%
'''
Below is a function named variance() that calculates the variance of a list of numbers. It
requires the mean of the list to be provided as an argument, just so we don't have to calculate
it more than once.
'''

# %%
# Calculate the variance of a list of numbers
def variance(values, mean):
	return sum([(x-mean)**2 for x in values])


# %%
'''
## Estimate Coefficients
We must estimate the values for two coefficients in simple linear regression.
We already have functions to calculate covariance() and variance(). Next, we need to
estimate a value for B0, also called the intercept as it controls the starting point of the line
where it intersects the y-axis.<br />
	B0 = mean(y) − B1 × mean(x)<br />
Again, we know how to estimate B1 and we have a function to estimate mean(). We can
put all of this together into a function named coefficients() that takes the dataset as an
argument and returns the coefficients.
'''

# %%
# Calculate coefficients
def coefficients(dataset):
	x = [row[0] for row in dataset]
	y = [row[1] for row in dataset]
	x_mean, y_mean = mean(x), mean(y)
	b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
	b0 = y_mean - b1 * x_mean
	return [b0, b1]


# %%
'''
Running this example calculates and prints the coefficients. Now that we know how to estimate the coefficients, the next step is to use them
'''


# %%
# calculate coefficients
dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
b0, b1 = coefficients(dataset)
print('Coefficients: B0=%.3f, B1=%.3f' % (b0, b1))