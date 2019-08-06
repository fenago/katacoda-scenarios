# %%
# Example of a Train-Test Test Harness
from random import seed
from random import randrange
from csv import reader


# %%
'''
## Train-Test Algorithm Test Harness
The train-test split is a simple resampling method that can be used to evaluate a machine
learning algorithm. As such, it is a good starting point for developing a test harness. <br />

Below  function takes a dataset and an algorithm and return a performance score. It takes 3 fixed arguments
including the dataset, the algorithm function and the split percentage for the train-test split.
First, the dataset is split into train and test elements. Next, a copy of the test set is made
and each output value is cleared by setting it to the None value to prevent the algorithm from
cheating accidentally.
'''

# %%
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

# Split a dataset into a train and test set
def train_test_split(dataset, split):
	train = list()
	train_size = split * len(dataset)
	dataset_copy = list(dataset)
	while len(train) < train_size:
		index = randrange(len(dataset_copy))
		train.append(dataset_copy.pop(index))
	return train, dataset_copy

# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0

# Evaluate an algorithm using a train/test split
def evaluate_algorithm(dataset, algorithm, split, *args):
	train, test = train_test_split(dataset, split)
	test_set = list()
	for row in test:
		row_copy = list(row)
		row_copy[-1] = None
		test_set.append(row_copy)
	predicted = algorithm(train, test_set, *args)
	actual = [row[-1] for row in test]
	accuracy = accuracy_metric(actual, predicted)
	return accuracy

# %%
'''
Let's piece this together with a worked example. We will use the Pima Indians Diabetes
dataset and evaluate the Zero Rule algorithm.
'''

# %%
# zero rule algorithm for classification
def zero_rule_algorithm_classification(train, test):
	output_values = [row[-1] for row in train]
	prediction = max(set(output_values), key=output_values.count)
	predicted = [prediction for i in range(len(test))]
	return predicted


# %%
'''
The dataset was split into 60% for training the model and 40% for evaluating it. Notice
how the name of the Zero Rule algorithm zero rule algorithm classification was passed
as an argument to the evaluate algorithm() function..Running the following example prints out the
accuracy of the model. <br />
Accuracy: 67.427%
'''


# %%
# Test the train/test harness
seed(1)
# load and prepare data
filename = 'pima-indians-diabetes.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])):
	str_column_to_float(dataset, i)
# evaluate algorithm
split = 0.6
accuracy = evaluate_algorithm(dataset, zero_rule_algorithm_classification, split)
print('Accuracy: %.3f%%' % (accuracy))