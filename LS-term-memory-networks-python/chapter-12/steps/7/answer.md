<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 7
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from matplotlib import pyplot
from pandas import DataFrame
from numpy import array

# return training data
def get_train():
	seq = [[1.0, 0.1], [1.0, 0.2], [1.0, 0.3], [1.0, 0.4], [1.0, 0.5]]
	seq = array(seq)
	X, y = seq[:, 0], seq[:, 1]
	X = X.reshape((5, 1, 1))
	return X, y

# return validation data
def get_val():
	seq = [[1.5, 0.6], [1.6, 0.7], [1.7, 0.8], [1.8, 0.9], [1.9, 1.0]]
	seq = array(seq)
	X, y = seq[:, 0], seq[:, 1]
	X = X.reshape((len(X), 1, 1))
	return X, y

# fit an LSTM model
def fit_model(n_cells):
	# define model
	model = Sequential()
	model.add(LSTM(n_cells, input_shape=(1,1)))
	model.add(Dense(1, activation='linear'))
	# compile model
	model.compile(loss='mse', optimizer='adam')
	# fit model
	X,y = get_train()
	model.fit(X, y, epochs=50, shuffle=False, verbose=0)
	# evaluate model
	valX, valY = get_val()
	loss = model.evaluate(valX, valY, verbose=0)
	return loss

# define scope of search
params = [1, 5, 10]
n_repeats = 3
# grid search parameter values
scores = DataFrame()
for value in params:
	# repeat each experiment multiple times
	loss_values = list()
	for i in range(n_repeats):
		loss = fit_model(value)
		loss_values.append(loss)
		print('>%d/%d param=%f, loss=%f' % (i+1, n_repeats, value, loss))
	# store results for this parameter
	scores[str(value)] = loss_values
# summary statistics of results
print(scores.describe())
# box and whisker plot of results
scores.boxplot()
pyplot.show()

</pre>

