# %%
'''
## Create Split
A split is comprised of an attribute in the dataset and a value. We can summarize this as the
index of an attribute to split and the value by which to split rows on that attribute. This is just
a useful shorthand for indexing into rows of data. Creating a split involves three parts, the first
we have already looked at which is calculating the Gini score. The remaining two parts are:
1. Splitting a Dataset.
2. Evaluating All Splits.
'''

# %%
'''
## 1. Splitting a Dataset
Splitting a dataset means separating a dataset into two lists of rows given the index of an
attribute and a split value for that attribute. Once we have the two groups, we can then use
our Gini score above to evaluate the cost of the split. Splitting a dataset involves iterating over
each row, checking if the attribute value is below or above the split value and assigning it to the
left or right group respectively. Below is a function named test split() that implements this
procedure.
'''


# %%
# Split a dataset based on an attribute and an attribute value
def test_split(index, value, dataset):
	left, right = list(), list()
	for row in dataset:
		if row[index] < value:
			left.append(row)
		else:
			right.append(row)
	return left, right


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
## 2. Evaluating All Splits
Given a dataset, we must check every value on each attribute as a candidate
split, evaluate the cost of the split and find the best possible split we could make. Once the
best split is found, we can use it as a node in our decision tree. <br />

Each group of data is its own small dataset of just those rows assigned to the left or right
group by the splitting process. You can imagine how we might split each group again, recursively
as we build out our decision tree. <br />

Below is a function named get split() that implements this
procedure. You can see that it iterates over each attribute (except the class value) and then
each value for that attribute, splitting and evaluating splits as it goes. The best split is recorded
and then returned after all checks are complete.
'''


# %%
# Select the best split point for a dataset
def get_split(dataset):
	class_values = list(set(row[-1] for row in dataset))
	b_index, b_value, b_score, b_groups = 999, 999, 999, None
	for index in range(len(dataset[0])-1):
		for row in dataset:
			groups = test_split(index, row[index], dataset)
			gini = gini_index(groups, class_values)
			print('X%d < %.3f Gini=%.3f' % ((index+1), row[index], gini))
			if gini < b_score:
				b_index, b_value, b_score, b_groups = index, row[index], gini, groups
	return {'index':b_index, 'value':b_value, 'groups':b_groups}


# %%
'''
We can contrive a small dataset to test out this function and our whole dataset splitting
process.
'''

# %%
# Test getting the best split
dataset = [[2.771244718,1.784783929,0],
	[1.728571309,1.169761413,0],
	[3.678319846,2.81281357,0],
	[3.961043357,2.61995032,0],
	[2.999208922,2.209014212,0],
	[7.497545867,3.162953546,1],
	[9.00220326,3.339047188,1],
	[7.444542326,0.476683375,1],
	[10.12493903,3.234550982,1],
	[6.642287351,3.319983761,1]]
split = get_split(dataset)
print('Split: [X%d < %.3f]' % ((split['index']+1), split['value']))