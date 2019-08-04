To complete this step, create a function named cross_validation_split() to split a dataset.
Create a copy of the dataset from which to draw randomly chosen rows and calculate the size of
each fold as the size of the dataset divided by the number of folds required.<br/>
            fold size = count(rows)/count(folds) 

<pre class="file" data-filename="cross_validation_split.py" data-target="replace">

# Example of Creating a Cross Validation Split
from random import seed
from random import randrange

# Split a dataset into k folds
def cross_validation_split(dataset, folds=3):
    # Write code here

</pre>

We can test this resampling method on the same small contrived dataset. Each
row has only a single column value, but we can imagine how this might scale to a standard
machine learning dataset.

<pre class="file" data-filename="cross_validation_split.py">

# test cross validation split
seed(1)
dataset = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
folds = cross_validation_split(dataset, 4)
print(folds)

</pre>

Now, run the python code by running: `python cross_validation_split.py`{{execute}}

**Note:** A k value of 4 is used for demonstration purposes. We would expect that the 10 rows divided into 4 folds will result in 2 rows per fold, with a remainder of 2 that will not be used in the split.