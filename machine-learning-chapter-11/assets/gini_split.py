# %%
'''
## Classification and Regression Trees 
CART for short is an acronym introduced by Leo Breiman
to refer to Decision Tree algorithms that can be used for classification or regression predictive
modeling problems. We will focus on using CART for classification in this tutorial. The
representation of the CART model is a binary tree.<br />

Creating a binary decision tree is actually a process of dividing up the input space. A greedy
approach is used called recursive binary splitting. This is a numerical procedure where all the
values are lined up and different split points are tried and tested using a cost function. The split
with the best cost (lowest cost because we minimize cost) is selected.<br />

- **Regression:** The cost function that is minimized to choose split points is the sum squared
error across all training samples that fall within the rectangle.
- **Classification:** The Gini cost function is used which provides an indication of how pure
the nodes are, where node purity refers to how mixed the training data assigned to each
node is.
'''


# %%
'''
## Gini Index
The Gini index is the name of the cost function used to evaluate splits in the dataset. A split
in the dataset involves one input attribute and one value for that attribute. It can be used to
divide training patterns into two groups of rows. <br />
A Gini score gives an idea of how good a split is by how mixed the classes are in the two
groups created by the split. A perfect separation results in a Gini score of 0, whereas the worst case split that results in 50/50 classes in each group results 
in a Gini score of 0.5<br />
'''

# %%
'''
Below is a function named gini_index() that calculates the Gini index for a list of groups
and a list of known class values. You can see that there are some safety checks in there to avoid
a divide by zero for an empty group.
'''

# %%
# Calculate the Gini index for a split dataset
def gini_index(groups, classes):
	# count all samples at split point
	n_instances = float(sum([len(group) for group in groups]))
	# sum weighted Gini index for each group
	gini = 0.0
	for group in groups:
		size = float(len(group))
		# avoid divide by zero
		if size == 0:
			continue
		score = 0.0
		# score the group based on the score for each class
		for class_val in classes:
			p = [row[-1] for row in group].count(class_val) / size
			score += p * p
		# weight the group score by its relative size
		gini += (1.0 - score) * (size / n_instances)
	return gini


# %%
'''
We can test above function with the following example. We can also test it for the worst
case of a 50/50 split in each group. The complete example is listed below.
'''

# %%
# Example of calculating Gini index
print(gini_index([[[1, 1], [1, 0]], [[1, 1], [1, 0]]], [0, 1]))
print(gini_index([[[1, 0], [1, 0]], [[1, 1], [1, 1]]], [0, 1]))
