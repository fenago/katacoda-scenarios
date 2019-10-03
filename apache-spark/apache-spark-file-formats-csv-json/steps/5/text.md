

**Step 3:** We can also use the modes we have learned in our theory. Let us see an example.

scala> val dataNew = spark
.read
.format(“csv”)
.options(Map(“InferSchema” -> “true”
, “header” -> “false”
, “nullValue” -> “Null”
, “mode” -> “FAILFAST”))
.load(“IdeaProjects/Spark/chapter_10/ratings.csv”)

scala> dataNew.show()


 
