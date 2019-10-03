
**Step 3:** Create a new Scala object and name it sqlJoins. Then import the following:

import org.apache.spark.sql.SparkSession

Then write the main function for our program and create a SparkSession object as shown below.



def main(args: Array[String]): Unit = {

  val spark = SparkSession
    .builder()
    .appName("SQL Joins")
    .master("local[*]")
    .getOrCreate()



