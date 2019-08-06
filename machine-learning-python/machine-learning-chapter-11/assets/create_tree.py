# %%
'''
## Building a Tree
Building the tree involves creating the root node and
calling the split() function that then calls itself recursively to build out the whole tree. Below
is the small build tree() function that implements this procedure.

We can test out this whole procedure using the small dataset we contrived above. Below is
the complete example. Also included is a small print tree() function that recursively prints
out nodes of the decision tree with one line per node. Although not as striking as a real decision
tree diagram, it gives an idea of the tree structure and decisions made throug
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
Below is a function named get split() that evaluaties splits. You can see that it iterates over each attribute (except the class value) and then
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
			if gini < b_score:
				b_index, b_value, b_score, b_groups = index, row[index], gini, groups
	return {'index':b_index, 'value':b_value, 'groups':b_groups}


# Create a terminal node value
def to_terminal(group):
	outcomes = [row[-1] for row in group]
	return max(set(outcomes), key=outcomes.count)


# %%
'''
## Recursive Splitting
Function split() is best explained in steps:
1. Firstly, the two groups of data split by the node are extracted for use and deleted from
the node. As we work on these groups the node no longer requires access to these data.
2. Next, we check if either left or right group of rows is empty and if so we create a terminal
node using what records we do have.
3. We then check if we have reached our maximum depth and if so we create a terminal node.
4. We then process the left child, creating a terminal node if the group of rows is too small,
otherwise creating and adding the left node in a depth first fashion until the bottom of
the tree is reached on this branch.
5. The right side is then processed in the same manner, as we rise back up the constructed
tree to the root.
'''

# %%
# Create child splits for a node or make terminal
def split(node, max_depth, min_size, depth):
	left, right = node['groups']
	del(node['groups'])
	# check for a no split
	if not left or not right:
		node['left'] = node['right'] = to_terminal(left + right)
		return
	# check for max depth
	if depth >= max_depth:
		node['left'], node['right'] = to_terminal(left), to_terminal(right)
		return
	# process left child
	if len(left) <= min_size:
		node['left'] = to_terminal(left)
	else:
		node['left'] = get_split(left)
		split(node['left'], max_depth, min_size, depth+1)
	# process right child
	if len(right) <= min_size:
		node['right'] = to_terminal(right)
	else:
		node['right'] = get_split(right)
		split(node['right'], max_depth, min_size, depth+1)

# Build a decision tree
def build_tree(train, max_depth, min_size):
	root = get_split(train)
	split(root, max_depth, min_size, 1)
	return root


# %%
'''
Function print_tree() function will recursively prints
out nodes of the decision tree with one line per node. Although not as striking as a real decision
tree diagram, it will give us an idea of the tree structure and decisions made throughout
'''

# %%
# Print a decision tree
def print_tree(node, depth=0):
	if isinstance(node, dict):
		print('%s[X%d < %.3f]' % ((depth*' ', (node['index']+1), node['value'])))
		print_tree(node['left'], depth+1)
		print_tree(node['right'], depth+1)
	else:
		print('%s[%s]' % ((depth*' ', node)))


# %%
'''
We can test out our procedure using the small dataset we contrived above. <br />

We can vary the maximum depth argument as we run this example and see the effect on the
printed tree. With a maximum depth of 1 (the second parameter in the call to the build_tree()
function), we can see that the tree uses the perfect split.
This is a tree with one node, also called a decision stump.
'''

# %%
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
tree = build_tree(dataset, 1, 1)
print_tree(tree)