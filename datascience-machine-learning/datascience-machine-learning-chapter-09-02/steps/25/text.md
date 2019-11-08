Going forward in Spark 2.0, MLlib is pushing dataframes as its primary API. This is the way of the future, so let's take a look at how it works. I've gone ahead and opened up the SparkLinearRegression.py file in Canopy, as shown in the following figure, so let's walk through it a little bit:

![](https://github.com/fenago/katacoda-scenarios/raw/master/datascience-machine-learning/datascience-machine-learning-chapter-09-02/steps/26/1.png)

As you see, for one thing, we're using ml instead of MLlib, and that's because the new dataframe-based API is in there.

#### Implementing linear regression
In this example, what we're going to do is implement linear regression, and linear regression is just a way of fitting a line to a set of data. What we're going to do in this exercise is take a bunch of fabricated data that we have in two dimensions, and try to fit a line to it with a linear model.

We're going to separate our data into two sets, one for building the model and one for evaluating the model, and we'll compare how well this linear model does at actually predicting real values. First of all, in Spark 2, if you're going to be doing stuff with the SparkSQL interface and using Datasets, you've got to be using a SparkSession object instead of a SparkContext. To set one up, you do the following:

```
spark = SparkSession.builder.config("spark.sql.warehouse.dir", "file:///C:/temp").appName("LinearRegression").getOrCreate() 
**Note:**

**Note:** that the middle bit is only necessary on Windows and in Spark 2.0. It kind of works around a little bug that they have, to be honest. So, if you're on Windows, make sure you have a C:/temp folder. If you want to run this, go create that now if you need to. If you're not on Windows, you can delete that whole middle section to leave: spark = SparkSession.builder.appName("LinearRegression").getOrCreate().

Okay, so you can say spark, give it an appName and getOrCreate().

This is interesting, because once you've created a Spark session, if it terminates unexpectedly, you can actually recover from that the next time that you run it. So, if we have a checkpoint directory, it can actually restart where it left off using getOrCreate.
