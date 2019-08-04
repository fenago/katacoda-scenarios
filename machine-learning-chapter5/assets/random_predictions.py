
# %%
# # Example of Making Random Predictions
from random import seed
from random import randrange



# %%
'''
## Random Prediction Algorithm
The random prediction algorithm predicts a random outcome as observed in the training data.
It is perhaps the simplest algorithm to implement. It requires that you store all of the distinct
outcome values in the training data, which could be large on regression problems with lots of
distinct values.
'''


# %%
# Generate random predictions
def random_algorithm(train, test):
	output_values = [row[-1] for row in train]
	unique = list(set(output_values))
	predicted = list()
	for _ in test:
		index = randrange(len(unique))
		predicted.append(unique[index])
	return predicted


# %%
'''
Running the example calculates random predictions for the test dataset and prints those
predictions.
'''


# %%
seed(1)
train = [[0], [1], [0], [1], [0], [1]]
test = [[None], [None], [None], [None]]
predictions = random_algorithm(train, test)
print(predictions)