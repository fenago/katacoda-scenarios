In this section, we will develop a model to classify face embeddings as one of the known celebrities
in the 5 Celebrity Faces Dataset. First, we must load the face embeddings dataset.

```
# load dataset
data = load(
'5-celebrity-faces-embeddings.npz
')
trainX, trainy, testX, testy = data[
'arr_0
'], data[
'arr_1
'], data[
'arr_2
'], data[
'arr_3
']
print(
'Dataset: train=%d, test=%d
' % (trainX.shape[0], testX.shape[0]))
```

Next, the data requires some minor preparation prior to modeling. First, it is a good practice
to normalize the face embedding vectors. It is a good practice because the vectors are often
compared to each other using a distance metric. In this context, vector normalization means
scaling the values until the length or magnitude of the vectors is 1 or unit length. This can
be achieved using the Normalizer class in scikit-learn. It might even be more convenient to
perform this step when the face embeddings are created in the previous step.

```
# normalize input vectors
in_encoder = Normalizer(norm=
'l2
')
trainX = in_encoder.transform(trainX)
testX = in_encoder.transform(testX)
```

Next, the string target variables for each celebrity name need to be converted to integers.
This can be achieved via the LabelEncoder class in scikit-learn.

```
# label encode targets
out_encoder = LabelEncoder()
out_encoder.fit(trainy)
trainy = out_encoder.transform(trainy)
testy = out_encoder.transform(testy)
```

Next, we can fit a model. It is common to use a Linear Support Vector Machine (SVM)
when working with normalized face embedding inputs. This is because the method is very
effective at separating the face embedding vectors. We can fit a linear SVM to the training
data using the SVC class in scikit-learn and setting the kernel argument to ‘linear’. We may
also want probabilities later when making predictions, which can be configured by setting the
probability argument to True.

```
# fit model
model = SVC(kernel=
'linear
')
model.fit(trainX, trainy)
```

Next, we can evaluate the model. This can be achieved by using the fit model to make a
prediction for each example in the train and test datasets and then calculating the classification
accuracy.

```
# predict
yhat_train = model.predict(trainX)
yhat_test = model.predict(testX)
# score
score_train = accuracy_score(trainy, yhat_train)
score_test = accuracy_score(testy, yhat_test)
# summarize
print(
'Accuracy: train=%.3f, test=%.3f
' % (score_train*100, score_test*100))
```
