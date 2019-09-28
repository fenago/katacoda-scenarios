<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab

# Example of Splitting a Contrived Dataset into Train and Test
from random import seed
from random import randrange

# Split a dataset into a train and test set
def train_test_split(dataset, split=0.60):
    train = list()
    train_size = split * len(dataset)
    dataset_copy = list(dataset)
    while len(train) < train_size:
        index = randrange(len(dataset_copy))
        train.append(dataset_copy.pop(index))
    return train, dataset_copy

# test train/test split
seed(0)
dataset = [[11], [12], [13], [14], [15], [16], [17], [18], [19], [20]]
train, test = train_test_split(dataset)
print(train)
print(test)

</pre>