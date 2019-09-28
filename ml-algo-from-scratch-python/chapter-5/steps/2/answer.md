<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# Example of Making Random Predictions
from random import seed
from random import randrange

# Generate random predictions
def random_algorithm(train, test):
    output_values = [row[-1] for row in train]
    unique = list(set(output_values))
    predicted = list()
    for _ in test:
        index = randrange(len(unique))
        predicted.append(unique[index])
    return predicted

seed(0)
train = [[1], [0], [1], [0], [1], [0]]
test = [[0], [0], [0], [0]]
predictions = random_algorithm(train, test)
print(predictions)

</pre>