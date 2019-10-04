

**Step 3:** Let us now declare a case class for the dataset we are about to load as shown below.

case class Ratings(userId: Int, movieID: Int, rating: Double, timeStamp: String)

Next, define the main function, create a Spark Session and load the file as dataset as shown below.

```
def main(args: Array[String]): Unit = {

  val spark = SparkSession
    .builder()
    .master("local[*]")
    .appName("Ratings Decrement UDF")
    .getOrCreate()
```

Make sure to import the implicts before you load the file as datset.

```
import spark.implicits._

val ratings = spark
  .read
  .format("csv")
  .options(Map("InferSchema" -> "true", "header" -> "true"))
  .load("chapter_9/ratings_head.csv")
  .as[Ratings]
```

The program should now look something like the screenshot below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 9/Selection_011.png)