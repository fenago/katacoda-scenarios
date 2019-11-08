
Now, we're going to use this regression.txt file that I have included with the course materials:

```
inputLines = spark.sparkContext.textFile("regression.txt")  
```

That is just a text file that has comma-delimited values of two columns, and they're just two columns of, more or less randomly, linearly correlated data. It can represent whatever you want. Let's imagine that it represents heights and weights, for example. So, the first column might represent heights, the second column might represent weights.

**Note:**

In the lingo of machine learning, we talk about labels and features, where labels are usually the thing that you're trying to predict, and features are a set of known attributes of the data that you use to make a prediction from.
