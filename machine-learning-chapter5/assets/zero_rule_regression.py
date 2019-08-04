# %%
# Example of Zero Rule Regression Predictions
from random import seed


# %%
'''
## Regression
Regression problems require the prediction of a real value. A good default prediction for real
values is to predict the central tendency. This could be the mean or the median. A good default
is to use the mean (also called the average) of the output value observed in the training data
'''


# %%
# zero rule algorithm for regression
def zero_rule_algorithm_regression(train, test):
	output_values = [row[-1] for row in train]
	prediction = sum(output_values) / float(len(output_values))
	predicted = [prediction for i in range(len(test))]
	return predicted


# %%
'''
Above function can be tested with a simple example. We can contrive a small dataset where
the mean value is known to be 15.

Below is the complete example. We would expect that the mean value of 15 will be predicted
for each of the 4 rows in the test dataset
'''


# %%
seed(1)
train = [[10], [15], [12], [15], [18], [20]]
test = [[None], [None], [None], [None]]
predictions = zero_rule_algorithm_regression(train, test)
print(predictions)