<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab in Step 3
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from numpy import array
from keras.models import model_from_json

# return training data
def get_train():
    seq = [[1.0, 0.1], [1.0, 0.2], [1.0, 0.3], [1.0, 0.4], [1.0, 0.5]]
    seq = array(seq)
    X, y = seq[:, 0], seq[:, 1]
    X = X.reshape((len(X), 1, 1))
    return X, y

# define model
model = Sequential()
model.add(LSTM(10, input_shape=(1,1)))
model.add(Dense(1, activation='linear'))
# compile model
model.compile(loss='mse', optimizer='adam')
# fit model
X,y = get_train()
model.fit(X, y, epochs=30, shuffle=False, verbose=0)
# convert model architecture to JSON format
architecture = model.to_json()
# save architecture to JSON file
with open('architecture.json', 'wt') as json_file:
    json_file.write(architecture)
# save weights to hdf5 file
model.save_weights('weights.h5')

# snip...
# later, perhaps run from another script

# load architecture from JSON File
json_file = open('architecture.json', 'rt')
architecture = json_file.read()
json_file.close()
# create model from architecture
model = model_from_json(architecture)
# load weights from hdf5 file
model.load_weights('weights.h5')
# make predictions
yhat = model.predict(X, verbose=0)
print(yhat)


</pre>
