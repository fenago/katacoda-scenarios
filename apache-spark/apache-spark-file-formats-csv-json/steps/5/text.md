

**Step 3:** We can also use the modes we have learned in our theory. Let us see an example.

Enter into the paste mode and execute the following code.
`:paste`{{execute T1}}

**Note:** After pasting following code in the scala terminal, Press  `Ctrl` + `D` to run code.

```val dataNew = spark
.read
.format("csv")
.options(Map("InferSchema" -> "true"
, "header" -> "false"
, "nullValue" -> "Null"
, "mode" -> "FAILFAST"))
.load("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/ratings.csv")```{{execute T1}}


`dataNew.show()`{{execute T1}}

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 10/Selection_009.png)


 
