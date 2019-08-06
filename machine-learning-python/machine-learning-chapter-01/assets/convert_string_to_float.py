# Example of converting string variables to float
from csv import reader

# Load a CSV file
def load_csv(filename):
	#write your code here

# Convert string column to float
def str_column_to_float(dataset, column):
	# write your code here

# Load pima-indians-diabetes dataset
filename = 'pima-indians-diabetes.csv'
dataset = load_csv(filename)
print('Loaded data file {0} with {1} rows and {2} columns'.format(filename, len(dataset), len(dataset[0])))
print(dataset[0])
# convert string columns to float
for i in range(len(dataset[0])):
	str_column_to_float(dataset, i)
print(dataset[0])