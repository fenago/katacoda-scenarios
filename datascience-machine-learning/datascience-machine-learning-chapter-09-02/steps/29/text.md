
I'm going to cache those results, and now I can just extract them and compare them together. So, let's pull out the prediction column, just using select like you would in SQL, and then I'm going to actually transform that dataframe and pull out the RDD from it, and use that to map it to just a plain old RDD full of floating point heights in this case:

```
predictions = fullPredictions.select("prediction").rdd.map(lambda x: x[0]) 
```

These are the predicted heights. Next, we're going to get the actual heights from the label column:

```
labels = fullPredictions.select("label").rdd.map(lambda x: x[0]) 
```

Finally, we can zip them back together and just print them out side by side and see how well it does:

```
predictionAndLabel = predictions.zip(labels).collect() 
 
for prediction in predictionAndLabel: 
    print(prediction) 
 
spark.stop() 
```

This is kind of a convoluted way of doing it; I did this to be more consistent with the previous example, but a simpler approach would be to just actually select prediction and label together into a single RDD that maps out those two columns together and then I don't have to zip them up, but either way it works. You'll also note that right at the end there we need to stop the Spark session.

So let's see if it works. Let's go up to Tools, Canopy Command Prompt, and we'll type in spark-submit SparkLinearRegression.py and let's see what happens.


#### Run Code
Now, run the python code by running: `python SparkLinearRegression.py`{{execute}}

There's a little bit more upfront time to actually run these APIs with Datasets, but once they get going, they're very fast. Alright, there you have it.

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-09-02/steps/26/2.png)

Here we have our actual and predicted values side by side, and you can see that they're not too bad. They tend to be more or less in the same ballpark. There you have it, a linear regression model in action using Spark 2.0, using the new dataframe-based API for MLlib. More and more, you'll be using these APIs going forward with MLlib in Spark, so make sure you opt for these when you can. Alright, that's MLlib in Spark, a way of actually distributing massive computing tasks across an entire cluster for doing machine learning on big Datasets. So, good skill to have. Let's move on.

