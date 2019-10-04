

**Step 3:** We can also use the modes we have learned in our theory. Let us see an example.

```val dataNew = spark
.read
.format("csv")
.options(Map("InferSchema" -> "true"
, "header" -> "false"
, "nullValue" -> "Null"
, "mode" -> "FAILFAST"))
.load("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/ratings.csv")```{{execute}}


`dataNew.show()`{{execute}}

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 10/Selection_009.png)


 
