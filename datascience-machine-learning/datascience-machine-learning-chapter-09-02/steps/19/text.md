We're going to start by importing the SparkConf and SparkContext libraries that we need for any Spark script that we run in Python, and then we're going to import HashingTF and IDF using the following commands.

```
from pyspark import SparkConf, SparkContext 
from pyspark.mllib.feature import HashingTF 
from pyspark.mllib.feature import IDF 
```

So, this is what computes the term frequencies (TF) and inverse document frequencies (IDF) within our documents.

#### Creating the initial RDD
We'll start off with our boilerplate Spark stuff that creates a local SparkConfiguration and a SparkContext, from which we can then create our initial RDD.

```
conf = SparkConf().setMaster("local").setAppName("SparkTFIDF") 
sc = SparkContext(conf = conf) 
```

Next, we're going to use our SparkContext to create an RDD from subset-small.tsv.

```
rawData = sc.textFile("e:/sundog-consult/Udemy/DataScience/subset-small.tsv") 
```

This is a file containing tab-separated values, and it represents a small sample of Wikipedia articles. Again, you'll need to change your path as shown in the preceding code as necessary for wherever you installed the course materials for this book.

That gives me back an RDD where every document is in each line of the RDD. The tsv file contains one entire Wikipedia document on every line, and I know that each one of those documents is split up into tabular fields that have various bits of metadata about each article.
