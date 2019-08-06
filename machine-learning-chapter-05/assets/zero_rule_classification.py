# %%
# Example of Zero Rule Classification Predictions
from random import seed


# %%
'''
## Zero Rule Algorithm
The Zero Rule Algorithm is a better baseline than the random algorithm. It uses more
information about a given problem to create one rule in order to make predictions. This rule is
different depending on the problem type. Let's start with classification problems, predicting a
class label.
'''

# %%
'''
## Classification
For classification problems, the one rule is to predict the class value that is most common in
the training dataset. This means that if a training dataset has 90 instances of class 0 and 10
instances of class 1 that it will predict 0 and achieve a baseline accuracy of 90/100 or 90%.
This is much better than the random prediction algorithm that would only achieve 82%
accuracy on average. For details on how this is estimate for random search is calculated, see
below:<br />
		= ((0:9 × 0:9) + (0:1 × 0:1)) × 100<br />
		= 82% (5.1)<br />
Below is a function named zero rule algorithm classification() that implements this
for the classification case.
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
Running the following example makes the predictions and prints them to screen. As expected, the
class value of 0 was chosen and predicted
'''


# %%
seed(1)
train = [['0'], ['0'], ['0'], ['0'], ['1'], ['1']]
test = [[None], [None], [None], [None]]
predictions = zero_rule_algorithm_classification(train, test)
print(predictions)