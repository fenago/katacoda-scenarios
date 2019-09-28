<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 4
# Example of Zero Rule Regression Predictions
from random import seed

# zero rule algorithm for regression
def zero_rule_algorithm_regression(train, test):
    output_values = [row[-1] for row in train]
    prediction = sum(output_values) / float(len(output_values))
    predicted = [prediction for i in range(len(test))]
    return predicted

seed(0)
train = [[20], [25], [22], [25], [28], [30]]
test = [[0], [0], [0], [0]]
predictions = zero_rule_algorithm_regression(train, test)
print(predictions)
</pre>

