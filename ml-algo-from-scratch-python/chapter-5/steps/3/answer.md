<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab in Step 3
# Example of Zero Rule Classification Predictions
from random import seed

# zero rule algorithm for classification
def zero_rule_algorithm_classification(train, test):
    output_values = [row[-1] for row in train]
    prediction = max(set(output_values), key=output_values.count)
    predicted = [prediction for i in range(len(test))]
    return predicted

seed(0)
train = [['1'], ['1'], ['1'], ['1'], ['0'], ['0']]
test = [[0], [0], [0], [0]]
predictions = zero_rule_algorithm_classification(train, test)
print(predictions)

</pre>
