# %%
# Example of calculating class probabilities
from math import sqrt
from math import pi
from math import exp


# %%
'''
## Class Probabilities
Now it is time to use the statistics calculated from our training data to calculate probabilities
for new data. Probabilities are calculated separately for each class. This means that we first
calculate the probability that a new piece of data belongs to the first class, then calculate
probabilities that it belongs to the second class, and so on for all the classes. The probability
that a piece of data belongs to a class is calculated as follows: <br />
P(class|data) = P(X|class) × P(class)
'''

# %%
# Split the dataset by class values, returns a dictionary
def separate_by_class(dataset):
	separated = dict()
	for i in range(len(dataset)):
		vector = dataset[i]
		class_value = vector[-1]
		if (class_value not in separated):
			separated[class_value] = list()
		separated[class_value].append(vector)
	return separated

# Calculate the mean of a list of numbers
def mean(numbers):
	return sum(numbers)/float(len(numbers))

# Calculate the standard deviation of a list of numbers
def stdev(numbers):
	avg = mean(numbers)
	variance = sum([(x-avg)**2 for x in numbers]) / float(len(numbers)-1)
	return sqrt(variance)

# Calculate the mean, stdev and count for each column in a dataset
def summarize_dataset(dataset):
	summaries = [(mean(column), stdev(column), len(column)) for column in zip(*dataset)]
	del(summaries[-1])
	return summaries

# Split dataset by class then calculate statistics for each row
def summarize_by_class(dataset):
	separated = separate_by_class(dataset)
	summaries = dict()
	for class_value, rows in separated.items():
		summaries[class_value] = summarize_dataset(rows)
	return summaries

# Calculate the Gaussian probability distribution function for x
def calculate_probability(x, mean, stdev):
	exponent = exp(-((x-mean)**2 / (2 * stdev**2 )))
	return (1 / (sqrt(2 * pi) * stdev)) * exponent


# %%
'''
Below is a function named calculate_class_probabilities() that will calculate class probabilities.<br />

First the total number of training records is calculated from the counts stored in the summary
statistics. This is used in the calculation of the probability of a given class or P(class) as the
ratio of rows with a given class of all rows in the training data. <br />

Next, probabilities are calculated for each input value in the row using the Gaussian
probability density function and the statistics for that column and of that class. Probabilities
are multiplied together as they accumulated. This process is repeated for each class in the
dataset. Finally a dictionary of probabilities is returned with one entry for each class. <br />
'''

# %%
# Calculate the probabilities of predicting each class for a given row
def calculate_class_probabilities(summaries, row):
	total_rows = sum([summaries[label][0][2] for label in summaries])
	probabilities = dict()
	for class_value, class_summaries in summaries.items():
		probabilities[class_value] = summaries[class_value][0][2]/float(total_rows)
		for i in range(len(class_summaries)):
			mean, stdev, _ = class_summaries[i]
			probabilities[class_value] *= calculate_probability(row[i], mean, stdev)
	return probabilities


# %%
'''
Let's run an example on the contrived dataset. The example below first calculates the summary statistics by class for the training dataset, then 
uses these statistics to calculate the probability of the first record belonging to each class.
'''

# %%
# Test calculating class probabilities
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
summaries = summarize_by_class(dataset)
probabilities = calculate_class_probabilities(summaries, dataset[0])
print(probabilities)

# %%
'''
Running the example prints the probabilities calculated for each class. We can see that the
probability of the first row belonging to the 0 class (0.0503) is higher than the probability of it
belonging to the 1 class (0.0001). We would therefore correctly conclude that it belongs to the 0
class.
'''