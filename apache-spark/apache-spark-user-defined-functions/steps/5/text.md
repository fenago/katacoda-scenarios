
Let's have a look how to write a user defined function. We will be writing a user defined function to decrease the rating of each movie by 0.5. We will be calling the UDF by using both Spark SQL and Dataframe APIs.

**Step 1:** Download the ratings_head.csv file from the URL below. This file contains four columns: userId, movieID, rating and timestamp.

ratings_head.csv - http://bit.ly/2X3r2wb

**Note:** We already have cloned a github repository which contains a required file. Open `apache-spark/Files/chapter_9` to view file.


**Step 2:** Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `apache-spark/src/main/scala/training/decrRatingUDF.scala` to view scala file.

```
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._
```

Next, let us define our user defined function using val keyword instead of using def keyword.

```
val decrUDF = udf((input: Double) => input - 0.5)
```

The syntax to define a function using val is a bit different than what we have been using so far with def function. Here we are simply assigning a function literal to an immutable variable. Also, we haven't specified the return type for the function as we can make use of Scala type inference to take care of the return type.


We are then passing the function literal inside the udf function. The udf  function takes a column as parameter and returns a column. Since we will be passing the entire column of our dataset Ratings as input to the decrUDF function in the application, we are using this udf function.

There are not many differences when it comes between val and def keyword to define functions. Please check the link in references section to learn more about val vs def.  

The program at this point of time should look like the screenshot as shown below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 9/Selection_010.png)