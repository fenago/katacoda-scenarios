<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution tab in Step 7
from math import sin
from math import pi
from math import exp
from random import randint
from random import uniform
from numpy import array
from matplotlib import pyplot
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense

# generate damped sine wave in [0,1]
def generate_sequence(length, period, decay):
	return [0.5 + 0.5 * sin(2 * pi * i / period) * exp(-decay * i) for i in range(length)]

# generate input and output pairs of damped sine waves
def generate_examples(length, n_patterns, output):
	X, y = list(), list()
	for _ in range(n_patterns):
		p = randint(10, 20)
		d = uniform(0.01, 0.1)
		sequence = generate_sequence(length + output, p, d)
		X.append(sequence[:-output])
		y.append(sequence[-output:])
	X = array(X).reshape(n_patterns, length, 1)
	y = array(y).reshape(n_patterns, output)
	return X, y

# configure problem
length = 25
output = 6

# define model
model = Sequential()
model.add(LSTM(20, return_sequences=True, input_shape=(length, 1)))
model.add(LSTM(20))
model.add(Dense(output))
model.compile(loss='mae', optimizer='adam')
model.summary()

# fit model
X, y = generate_examples(length, 100, output)
history = model.fit(X, y, batch_size=10, epochs=1)

# evaluate model
X, y = generate_examples(length, 10, output)
loss = model.evaluate(X, y, verbose=0)
print('MAE: %f' % loss)

# prediction on new data
X, y = generate_examples(length, 1, output)
yhat = model.predict(X, verbose=0)
pyplot.plot(y[0], label='y')
pyplot.plot(yhat[0], label='yhat')
pyplot.legend()
pyplot.show()
</pre>

