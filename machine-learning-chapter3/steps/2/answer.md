<pre class="file" data-filename="split_train_test.py" data-target="replace">

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
seed(1)
dataset = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
train, test = train_test_split(dataset)
print(train)
print(test)

</pre>

#### Overview
- The function first calculates how many rows the training set requires from the provided
dataset. 
- A copy of the original dataset is made. 
= Random rows are selected and removed from the copied dataset and added to the train dataset 
- Rows that remain in the copy of the dataset are then returned as the test dataset.