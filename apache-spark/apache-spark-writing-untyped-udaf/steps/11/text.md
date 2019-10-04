
**Step 2:** Let us now register the UDAF with Spark.

```
sparkSession.udf.register("averageUDAF", averageUDAF)
```

**Step 3:** Let us now read the file and create a temporary view on the DataFrame to write SQL queries.
 
```
val ratings = sparkSession.read
	.format("csv")
	.options(Map("InferSchema" -> "true", "header" -> "true"))
  .load("chapter_9/ratings_head.csv")

ratings.createOrReplaceTempView("ratings")
```
