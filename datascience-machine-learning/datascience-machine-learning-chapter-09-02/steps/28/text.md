
Now, like I said, we're going to split our data in half.

```
trainTest = df.randomSplit([0.5, 0.5]) 
trainingDF = trainTest[0] 
testDF = trainTest[1] 
```

We're going to do a 50/50 split between training data and test data. This returns back two dataframes, one that I'm going to use to actually create my model, and one that I'm going to use to evaluate my model.

I will next create my actual linear regression model with a few standard parameters here that I've set.

```
lir = LinearRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)
``` 

We're going to call lir = LinearRegression, and then I will fit that model to the set of data that I held aside for training, the training data frame:

```
model = lir.fit(trainingDF) 
```

That gives me back a model that I can use to make predictions from.

Let's go ahead and do that.

```
fullPredictions = model.transform(testDF).cache() 
```

I will call model.transform(testDF), and what that's going to do is predict the heights based on the weights in my testing Dataset. I actually have the known labels, the actual, correct heights, and this is going to add a new column to that dataframe called predictions, that has the predicted values based on that linear model.
