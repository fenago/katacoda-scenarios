**Step 8:** Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `apache-spark/src/main/scala/training/countByMovieMain.scala` to view scala file.

```
import org.apache.spark.sql.SparkSession
```

Let us first create a case class with all our fields for input data outside the object as shown in the screenshot below.

```
case class Movies(userId: Int, movieId: Int, rating : Double, timeStamp: String)
```



**Step 9:** Let us now write our main function and create a SparkSession object. 

```
def main(args: Array[String]) {

  val sparkSession = SparkSession.builder.
    master("local[*]")
    .appName("Count By movieId")
    .getOrCreate()
```

Next, let us create the Accumulator object and register it using the register method as shown below. We have to register out Accumulator since it is custom accumulator. You will not have to register for the built-in accumulators.

```
val countByMovie = new CountByMovie()
sparkSession.sparkContext.register(countByMovie)
```

