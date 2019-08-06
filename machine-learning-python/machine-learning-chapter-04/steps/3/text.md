To complete this step, create a function named confusion_matrix() to calculate the confusion matrix given a list of actual class values and a list of predictions. It shoulf first make a list of all of the unique class values and assigns each class value a unique integer or index into the confusion matrix

<pre class="file" data-filename="confusion_matrix.py" data-target="replace">

# Example of Calculating a Confusion Matrix

# calculate a confusion matrix
def confusion_matrix(actual, predicted):
    # Write code here

</pre>

We can test the above method on the small contrived dataset. Below is contrived dataset with 3 mistakes.

<pre class="file" data-filename="confusion_matrix.py">

# Test confusion matrix with integers
actual = [0,0,0,0,0,1,1,1,1,1]
predicted = [0,1,1,0,0,1,0,1,1,1]
unique, matrix = confusion_matrix(actual, predicted)
print(unique)
print(matrix)

</pre>

Now, run the python code by running: `python confusion_matrix.py`{{execute}}

It's hard to interpret the results this way. It would help if we could display the matrix as
intended with rows and columns. We will modify code in the next step.