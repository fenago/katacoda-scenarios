For each bootstrap sample taken from the training data, there will be samples left behind that
were not included. These samples are called Out-Of-Bag samples or OOB. The performance of
each model on its left out samples when averaged can provide an estimated accuracy of the bagged
models. This estimated performance is often called the OOB estimate. These performance
measures are a reliable estimate of test error and correlate well with cross-validation estimates
of error.

#### Variable Importance
As the Bagged decision trees are constructed, we can calculate how much the error function
drops for a variable at each split point. In regression problems this may be the drop in sum
squared error and in classification this might be the Gini score. These drops in error can be
averaged across all decision trees and output to provide an estimate of the importance of each
input variable. The greater the drop when the variable was chosen, the greater the importance.
These outputs can help identify subsets of input variables that may be most or least relevant
to the problem and suggest at possible feature selection experiments you could perform where
some features are removed from the dataset


#### Preparing Data For Bagged CART
Bagged CART does not require any special data preparation other than a good representation
of the problem.