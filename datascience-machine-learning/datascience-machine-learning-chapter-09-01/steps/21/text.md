
Creating a test candidate and building our decision tree
Let's create a little test candidate we can use, so we can use our model to actually predict whether someone new would be hired or not. What we're going to do is create a test candidate that consists of an array of the same values for each field as we had in the CSV file:

```
testCandidates = [ array([10, 1, 3, 1, 0, 0])] 
```

Let's quickly compare that code with the Excel document so you can see the array mapping:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-09-01/steps/12/6.png)

Again, we need to map these back to their original column representation, so that 10, 1, 3, 1, 0, 0 means 10 years of prior experience, currently employed, three previous employers, a BS degree, did not go to a top-tier school and did not do an internship. We could actually create an entire RDD full of candidates if we wanted to, but we'll just do one for now.

Next, we'll use parallelize to convert that list into an RDD:

```
testData = sc.parallelize(testCandidates) 
```

Nothing new there. Alright, now for the magic let's move to the next code block:

```
model = DecisionTree.trainClassifier(trainingData, numClasses=2, 
                    categoricalFeaturesInfo={1:2, 3:4, 4:2, 5:2}, 
                    impurity='gini', maxDepth=5, maxBins=32) 
```

We are going to call DecisionTree.trainClassifier, and this is what will actually build our decision tree itself. We pass in our trainingData, which is just an RDD full of LabeledPoint arrays, numClasses=2, because we have, basically, a yes or no prediction that we're trying to make, will this person be hired or not? The next parameter is called categoricalFeaturesInfo, and this is a Python dictionary that maps fields to the number of categories in each field. So, if you have a continuous range available to a given field, like the number of years of experience, you wouldn't specify that at all in here, but for fields that are categorical in nature, such as what degree do they have, for example, that would say fieldID3, mapping to the degree attained, which has four different possibilities: no education, BS, MS, and PhD. For all of the yes/no fields, we're mapping those to 2 possible categories, yes/no or 0/1 is what we converted those to.

Continuing to move through our DecisionTree.trainClassifier call, we are going to use the 'gini' impurity metric as we measure the entropy. We have a maxDepth of 5, which is just an upper boundary on how far we're going to go, that can be larger if you wish. Finally, maxBins is just a way to trade off computational expense if you can, so it just needs to at least be the maximum number of categories you have in each feature. Remember, nothing really happens until we call an action, so we're going to actually use this model to make a prediction for our test candidate.

We use our DecisionTree model, which contains a decision tree that was trained on our test training data, and we tell that to make a prediction on our test data:

```
predictions = model.predict(testData) 
print ('Hire prediction:') 
results = predictions.collect() 
for result in results: 
     print (result) 
```

We'll get back a list of predictions that we can then iterate through. So, predict returns a plain old Python object and is an action that I can collect. Let me rephrase that a little bit: collect will return a Python object on our predictions, and then we can iterate through every item in that list and print the result of the prediction.

We can also print out the decision tree itself by using toDebugString:

```
print('Learned classification tree model:') 
print(model.toDebugString()) 
```

That will actually print out a little representation of the decision tree that it created internally, that you can follow through in your own head. So, that's kind of cool too.


