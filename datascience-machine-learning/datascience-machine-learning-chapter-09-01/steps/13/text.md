First, we're going to import, from pyspark.mllib, the bits that we need from the machine learning library for Spark.

```
from pyspark.mllib.regression import LabeledPoint 
from pyspark.mllib.tree import DecisionTree 
```

We need the LabeledPoint class, which is a data type required by the DecisionTree class, and the DecisionTree class itself, imported from mllib.tree.

Next, pretty much every Spark script you see is going to include this line, where we import SparkConf and SparkContext:

```
from pyspark import SparkConf, SparkContext 
```

This is needed to create the SparkContext object that is kind of the root of everything you do in Spark.

And finally, we're going to import the array library from numpy:

```
from numpy import array 
```

Yes, you can still use NumPy, and scikit-learn, and whatever you want within Spark scripts. You just have to make sure, first of all, that these libraries are installed on every machine that you intend to run it on.

If you're running on a cluster, you need to make sure that those Python libraries are already in place somehow, and you also need to understand that Spark will not make the scikit-learn methods, for example, magically scalable. You can still call these functions in the context of a given map function, or something like that, but it's only going to run on that one machine within that one process. Don't lean on that stuff too heavily, but, for simple things like managing arrays, it's totally an okay thing to do.
