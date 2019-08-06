# %%
# Example of subsampling a dataste
from random import seed
from random import randrange


# %%
'''
## Bootstrap Resample
Let's start off by getting a strong idea of how the bootstrap method works. We can create a
new sample of a dataset by randomly selecting rows from the dataset and adding them to a new
list. We can repeat this for a fixed number of rows or until the size of the new dataset matches
a ratio of the size of the original dataset.

We can allow sampling with replacement by not removing the row that was selected so that
it is available for future selections. Below is a function named subsample() that implements
this procedure. The randrange() function from the random module is used to select a random
row index to add to the sample each iteration of the loop. The default size of the sample is the
size of the original dataset.
'''

# %%
# Create a random subsample from the dataset with replacement
def subsample(dataset, ratio=1.0):
	sample = list()
	n_sample = round(len(dataset) * ratio)
	while len(sample) < n_sample:
		index = randrange(len(dataset))
		sample.append(dataset[index])
	return sample

# Calculate the mean of a list of numbers
def mean(numbers):
	return sum(numbers) / float(len(numbers))


# %%
'''
We can use this function to estimate the mean of a contrived dataset. First, we can create a
dataset with 20 rows and a single column of random numbers between 0 and 9 and calculate the16.2. Tutorial 178
mean value. We can then make bootstrap samples of the original dataset, calculate the mean,
and repeat this process until we have a list of means. Taking the average of these sample means
should give us a robust estimate of the mean of the entire dataset.

Each bootstrap sample is created as a 10% sample of
the original 20 observation dataset (or 2 observations). We then experiment by creating 1, 10,
100 bootstrap samples of the original dataset, calculate their mean value, then average all of
those estimated mean values
'''


# %%
# Test subsampling a dataset
seed(1)
# True mean
dataset = [[randrange(10)] for i in range(20)]
print('True Mean: %.3f' % mean([row[0] for row in dataset]))
# Estimated means
ratio = 0.10
for size in [1, 10, 100]:
	sample_means = list()
	for i in range(size):
		sample = subsample(dataset, ratio)
		sample_mean = mean([row[0] for row in sample])
		sample_means.append(sample_mean)
	print('Samples=%d, Estimated Mean: %.3f' % (size, mean(sample_means)))

# %%
'''
Running the above example prints the original mean value we aim to estimate. We can then see
the estimated mean from the various different numbers of bootstrap samples. We can see that
with 100 samples we achieve a good estimate of the mean.
'''
