**Step 4:** Let us now read both the files as shown below.

```
val movies = spark.read
  .format("csv")
  .options(Map("inferSchema" -> "true", "header" -> "true"))
  .load("chapter_7/movies-head.csv")
val ratings = spark.read

  .format("csv")
  .options(Map("inferSchema" -> "true", "header" -> "true"))
  .load("chapter_7/ratings-head.csv")
```

We now have two dataFrames for each of our input file.

 
