
**Step 8:** Create a new object by right-clicking the training package which you have created in previous exercises and hover over New and then click on Scala Class. When prompted, enter countByMovieMain as the name and click on the dropdown for Kind and select Object. Enter the import as shown below.

import org.apache.spark.sql.SparkSession

Let us first create a case class with all our fields for input data outside the object as shown in the screenshot below.

case class Movies(userId: Int, movieId: Int, rating : Double, timeStamp: String)






 

**Step 9:** Let us now write our main function and create a SparkSession object. 

def main(args: Array[String]) {

  val sparkSession = SparkSession.builder.
    master("local[*]")
    .appName("Count By movieId")
    .getOrCreate()

Next, let us create the Accumulator object and register it using the register method as shown below. We have to register out Accumulator since it is custom accumulator. You will not have to register for the built-in accumulators.

val countByMovie = new CountByMovie()
sparkSession.sparkContext.register(countByMovie)


