<pre class="file" data-target="clipboard">
# Hint: You can copy Solution to ClipBoard from Solution Tab
# Train XGBoost model, save to file using joblib, load and make predictions
from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# load data
dataset = loadtxt('african-diabetes.csv', delimiter=",")
# split data into X and y
X = dataset[:,0:8]
Y = dataset[:,8]
# split data into train and test sets
seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
# fit model on training data
model = XGBClassifier()
model.fit(X_train, y_train)
# save model to file
joblib.dump(model, "african.joblib.dat")
print("Saved model to: african.joblib.dat")

# some time later...

# load model from file
loaded_model = joblib.load("african.joblib.dat")
print("Loaded model from: african.joblib.dat")
# make predictions for test data
predictions = loaded_model.predict(X_test)
# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))


</pre>
