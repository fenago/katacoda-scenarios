**Step 10:** Let us now write some code to read the input data. We will also need to import the implicits.

```
import sparkSession.implicits._

val options = Map("header" -> "true", "inferSchema" -> "true")

val data = sparkSession.read.format("com.databricks.spark.csv")
.options(cvsOptions)
.load(input)
.as[User]
```

Do not worry if this code doesn't make sense. Just think this as a way to read the input data, as we used to do with SparkContext object in the previous exercises. Everything will start to make sense once we cover the next couple of chapters.

 

 

**Step 11:** Let us now apply our custom accumulator in the foreach higher order function and print the result to console.

```
data.foreach(record => {
      countByMovie.add((record.location, 1))
    })

    println(countByMovie.value.toList)

  }
}
```

Here, we are passing our data through the foreach function, where our custom accumulator countByMovie is applied with the add method. We specify the movieId as the field for which the aggregations to be done on. Finally, we can access the result by calling value method on our custom accumulator and convert it to a List.
