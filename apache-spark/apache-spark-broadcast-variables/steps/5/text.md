**Step 2:** Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `apache-spark/src/main/scala/training/ratingsByMovies.scala` to view scala file.


```
import org.apache.spark.SparkContext
import scala.io.Source
```

The first import is as we know to create the SparkContext object. The second is Scala specific import which helps us read the movies.csv file.
 
Let us now define a function which would load the movie names to a Map object.

```
def loadMovieNames(): Map[Int, String] = {

  var movieNames: Map[Int, String] = Map()

  val data = Source.fromFile("chapter_6/movies.csv").getLines()
  for (record <- data) {
    val fields = record.split(',')
    if (fields.length > 1) {
      movieNames += (fields(0).toInt -> fields(1))
    }
  }
  movieNames
}
```

We are defining a function called loadMovieNames which does not take any arguments and returns a Map object which maps Int to String. We then declare a movieNames variable of type Map which maps Int to String and initialize it as an empty map.

Next, we load the data from our file using Source.fromFile method and call getlines method to get each line based on /n character. Next, we iterate through each record in our input data using the for comprehension, and split each field based on comma as we know our fields are delimited by a comma. Next, we check if each record has two fields and finally map movie Id with the movie name, by adding the fields to movieNames Map object. Finally, return the Map object as required by our function.
