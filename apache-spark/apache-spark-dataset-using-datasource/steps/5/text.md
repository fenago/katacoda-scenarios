
**Step 4:** Before, we load the file using the DataSource API, we neet to import the implicits. This import is required to create a Dataset.

```
import spark.implicits._
```

This import is available in our SparkSession object. Hence we refer it with the SparkSession object (spark) which we created in the previous step.


Now, we load the file as we usually do while creating the DataFrame except for the as method at the end. The as method refers to the case class object Movies creating a Dataset object.

```
val movies = spark
  .read
  .format("csv")
  .options(Map("header" -> "true", "inferSchema" -> "true"))
  .load("chapter_8/ratings-head.csv")
  .as[Movies]
  .cache()
```
 

We use the cache method to cache our Dataset in memory so that it does get created everytime an action is called. You now have your Dataset created.
