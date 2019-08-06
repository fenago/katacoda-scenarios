# %%
'''
## Naive Bayes
Bayes Theorem provides a way that we can calculate the probability of a piece of data belonging
to a given class, given our prior knowledge. Bayes Theorem is stated as:<br />
P(class|data) = P(data|class) × P(class)/ P(data)
'''

# %%
'''
## Separate By Class
We will need to calculate the probability of data by the class they belong to. This means that
we will first need to separate our training data by class. A relatively straightforward operation.
We can create a dictionary object where each key is the class value and then add a list of all the
records as the value in the dictionary. Below is a function named separate_by_class() that
implements this approach. It assumes that the last column in each row is the class value.
'''

# %%
# Split the dataset by class values, returns a dictionary
def separate_by_class(dataset):
	separated = dict()
	for i in range(len(dataset)):
		vector = dataset[i]
		class_value = vector[-1]
		if (class_value not in separated):
			separated[class_value] = list()
		separated[class_value].append(vector)
	return separated


# %%
'''
we can test our separate_by_class function on the contrived dataset.

Running the example sorts observations in the dataset by their class value, then prints the
class value followed by all identified records.
'''

# %%
# Test separating data by class
dataset = [[3.393533211,2.331273381,0],
	[3.110073483,1.781539638,0],
	[1.343808831,3.368360954,0],
	[3.582294042,4.67917911,0],
	[2.280362439,2.866990263,0],
	[7.423436942,4.696522875,1],
	[5.745051997,3.533989803,1],
	[9.172168622,2.511101045,1],
	[7.792783481,3.424088941,1],
	[7.939820817,0.791637231,1]]
separated = separate_by_class(dataset)
for label in separated:
	print(label)
	for row in separated[label]:
		print(row)