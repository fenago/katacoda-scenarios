# %%
# Stacking on the sonar dataset
from random import seed
from random import randrange
from csv import reader
from math import sqrt
from math import exp


# %%
'''
## Stacked Generalization
Stacked Generalization or stacking is an ensemble technique that uses a new model to learn how to best combine the predictions from two or more
models trained on your dataset.

Stacked Generalization is an ensemble algorithm where a new model is trained to combine the
predictions from two or more models already trained or your dataset. The predictions from the
existing models or submodels are combined using a new model, and as such stacking is often
referred to as blending, as the predictions from submodels are blended together.
'''

# %%
'''
## Sonar Dataset
In this section, we will apply the Stacking algorithm to the Sonar dataset. The example assumes that a CSV copy of the dataset is in the current 
working directory with the filename sonar.all-data.csv.

The dataset is first loaded, the string values converted to numeric and the output column is converted from strings to the integer values of 0 to 1.
This is achieved with helper functions load csv(), str column to float() and str column to int() to load and prepare the dataset
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

# Convert string column to integer
def str_column_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup


# %%
'''
We will use k-fold cross-validation to estimate the performance of the learned model on
unseen data. This means that we will construct and evaluate k models and estimate the
performance as the mean model error. Classification accuracy will be used to evaluate the
model. These behaviors are provided in the cross validation split(), accuracy metric()
and evaluate algorithm() helper functions.
'''

# %%
# Split a dataset into k folds
def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	for _ in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split

# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0

# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
	folds = cross_validation_split(dataset, n_folds)
	scores = list()
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = list()
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None
		predicted = algorithm(train_set, test_set, *args)
		actual = [row[-1] for row in fold]
		accuracy = accuracy_metric(actual, predicted)
		scores.append(accuracy)
	return scores

# %%
'''
## Submodels and Aggregator
We are going to use two models as submodels for stacking and a linear model as the aggregator
model.
This part is divided into 3 sections:
1. Submodel #1: k-Nearest Neighbors.
2. Submodel #2: Perceptron.
3. Aggregator Model: Logistic Regression.
'''

# %%
'''
Below are the helper functions that involve making predictions for a KNN model. The function euclidean distance() calculates the distance between two rows of data, get neighbors()
function locates all neighbors in the training dataset for a new row of data and knn predict()
makes a prediction from the neighbors for a new row of data.
'''

# %%
# Calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += (row1[i] - row2[i])**2
	return sqrt(distance)

# Locate neighbors for a new row
def get_neighbors(train, test_row, num_neighbors):
	distances = list()
	for train_row in train:
		dist = euclidean_distance(test_row, train_row)
		distances.append((train_row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors

# Make a prediction with kNN
def knn_predict(model, test_row, num_neighbors=2):
	neighbors = get_neighbors(model, test_row, num_neighbors)
	output_values = [row[-1] for row in neighbors]
	prediction = max(set(output_values), key=output_values.count)
	return prediction

# %%
'''
## Submodel #1: k-Nearest Neighbors
The k-Nearest Neighbors algorithm or KNN uses the entire training dataset as the model.
Therefore training the model involves retaining the training dataset. Below is a function named
knn model() that does just this.
'''

# %%
# Prepare the kNN model
def knn_model(train):
	return train


# %%
'''
## Submodel #2: Perceptron
The model for the Perceptron algorithm is a set of weights learned from the training data. In
order to train the weights, many predictions need to be made on the training data in order
to calculate error values. Therefore, both model training and prediction require a function for
prediction.
Below are the helper functions for implementing the Perceptron algorithm. The perceptron model()
function trains the Perceptron model on the training dataset and perceptron predict() is
used to make a prediction for a row of data
'''

# %%
# Make a prediction with weights
def perceptron_predict(model, row):
	activation = model[0]
	for i in range(len(row)-1):
		activation += model[i + 1] * row[i]
	return 1.0 if activation >= 0.0 else 0.0

# Estimate Perceptron weights using stochastic gradient descent
def perceptron_model(train, l_rate=0.01, n_epoch=5000):
	weights = [0.0 for i in range(len(train[0]))]
	for _ in range(n_epoch):
		for row in train:
			prediction = perceptron_predict(weights, row)
			error = row[-1] - prediction
			weights[0] = weights[0] + l_rate * error
			for i in range(len(row)-1):
				weights[i + 1] = weights[i + 1] + l_rate * error * row[i]
	return weights


# %%
'''
## Aggregator Model: Logistic Regression
Like the Perceptron algorithm, Logistic Regression uses a set of weights, called coefficients, as
the representation of the model. And like the Perceptron algorithm, the coefficients are learned
by iteratively making predictions on the training data and updating them.
Below are the helper functions for implementing the logistic regression algorithm. The
logistic regression model() function is used to train the coefficients on the training dataset
and logistic regression predict() is used to make a prediction for a row of data.
'''

# %%
# Make a prediction with coefficients
def logistic_regression_predict(model, row):
	yhat = model[0]
	for i in range(len(row)-1):
		yhat += model[i + 1] * row[i]
	return 1.0 / (1.0 + exp(-yhat))

# Estimate logistic regression coefficients using stochastic gradient descent
def logistic_regression_model(train, l_rate=0.01, n_epoch=5000):
	coef = [0.0 for i in range(len(train[0]))]
	for _ in range(n_epoch):
		for row in train:
			yhat = logistic_regression_predict(coef, row)
			error = row[-1] - yhat
			coef[0] = coef[0] + l_rate * error * yhat * (1.0 - yhat)
			for i in range(len(row)-1):
				coef[i + 1] = coef[i + 1] + l_rate * error * yhat * (1.0 - yhat) * row[i]
	return coef

# Make predictions with sub-models and construct a new stacked row
def to_stacked_row(models, predict_list, row):
	stacked_row = list()
	for i in range(len(models)):
		prediction = predict_list[i](models[i], row)
		stacked_row.append(prediction)
	stacked_row.append(row[-1])
	return row[0:len(row)-1] + stacked_row


# %%
'''
Below function named stacking() does 4 things:
1. It first trains a list of models (KNN and Perceptron).
2. It then uses the models to make predictions and create a new stacked dataset.
3. It then trains an aggregator model (logistic regression) on the stacked dataset.
4. It then uses the submodels and aggregator model to make predictions on the test dataset
'''

# %%
# Stacked Generalization Algorithm
def stacking(train, test):
	model_list = [knn_model, perceptron_model]
	predict_list = [knn_predict, perceptron_predict]
	models = list()
	for i in range(len(model_list)):
		model = model_list[i](train)
		models.append(model)
	stacked_dataset = list()
	for row in train:
		stacked_row = to_stacked_row(models, predict_list, row)
		stacked_dataset.append(stacked_row)
	stacked_model = logistic_regression_model(stacked_dataset)
	predictions = list()
	for row in test:
		stacked_row = to_stacked_row(models, predict_list, row)
		stacked_dataset.append(stacked_row)
		prediction = logistic_regression_predict(stacked_model, stacked_row)
		prediction = round(prediction)
		predictions.append(prediction)
	return predictions


# %%
'''
A k value of 3 was used for cross-validation, giving each fold 208/3 = 69.3  or just under 70
records to be evaluated upon each iteration. Running the example prints the scores and mean
of the scores for the final configuration.
'''

# %%
# Test stacking on the sonar dataset
seed(1)
# load and prepare data
filename = 'sonar.all-data.csv'
dataset = load_csv(filename)
# convert string attributes to integers
for i in range(len(dataset[0])-1):
	str_column_to_float(dataset, i)
# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)
n_folds = 3
scores = evaluate_algorithm(dataset, stacking, n_folds)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))