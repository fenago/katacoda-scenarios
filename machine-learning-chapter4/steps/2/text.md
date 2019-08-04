To complete this step, create a function that takes the expected outcomes and the predictions
as arguments. It will returns classification accuracy as a percentage.<br/>
        accuracy = correct predictions/total predictions × 100

<pre class="file" data-filename="classification_accuracy.py" data-target="replace">

# Example of calculating classification accuracy

# Calculate accuracy percentage between two lists
def accuracy_metric(actual, predicted):
    # Write code here

</pre>

We can contrive a small dataset to test this function. Below are a set of 10 actual and
predicted integer values. There are two mistakes in the set of predictions.

<pre class="file" data-filename="classification_accuracy.py">

# Test accuracy
actual = [0,0,0,0,0,1,1,1,1,1]
predicted = [0,1,0,0,0,1,0,1,1,1]
accuracy = accuracy_metric(actual, predicted)
print(accuracy)

</pre>

Now, run the python code by running: `python classification_accuracy.py`{{execute}}
