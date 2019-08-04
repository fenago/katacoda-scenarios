To complete this step, create a function named train test split() to split a dataset into a train and test split.
It accepts two arguments: the dataset to split as a list of lists and an optional split percentage.
A default split percentage of 0.6 or 60% is used. This will assign 60% of the dataset to the
training dataset and leave the remaining 40% to the test dataset.

<pre class="file" data-filename="split_train_test.py" data-target="replace">

# Example of Splitting a Contrived Dataset into Train and Test
from random import seed
from random import randrange

# Split a dataset into a train and test set
def train_test_split(dataset, split=0.60):
    # Write code here

</pre>

We can test this function using a contrived dataset of 10 rows, each with a single column.
The complete example is listed below.

<pre class="file" data-filename="split_train_test.py">

# test train/test split
seed(1)
dataset = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
train, test = train_test_split(dataset)
print(train)
print(test)

</pre>

Now, run the python code by running: `python split_train_test.py`{{execute}}