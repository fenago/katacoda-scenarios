
**Step 3:** Now, write the main function and create the SparkSession object as shown below.

```
def main(args: Array[String]): Unit = {

  val spark = SparkSession
    .builder()
    .appName("Creating a Dataset")
    .master("local[*]")
    .getOrCreate()
```

Next import the implicits and load the file as shown below.

```
import spark.implicits._

val employeeDS = spark.read
  .format("csv")
  .options(Map("header" -> "true", "inferSchema" -> "true"))
  .load("chapter_8/employee.csv")
  .as[Employee]
```

Your program should like something like the one shown in screenshot.




 