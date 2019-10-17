
**Step 3:** Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `apache-spark/src/main/scala/training/sqlJoins.scala` to view scala file.

```
import org.apache.spark.sql.SparkSession
```

Then write the main function for our program and create a SparkSession object as shown below.

```
def main(args: Array[String]): Unit = {

  val spark = SparkSession
    .builder()
    .appName("SQL Joins")
    .master("local[*]")
    .getOrCreate()
```




