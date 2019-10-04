
 
**Step 3:** Let us now create a case class so that we can define schema to our dataFrame. The names which we specify for attributes of case class object will get mapped as column names for our dataFrame. This will make sense when we run the program.

```
case class Players(player_name: String, team: String, position: String, height: Int, weight: Int, age: Double)
```

**Step 4:** Let us now write the main function for our program and create a SparkSession object as shown below.

```
def main(args: Array[String]): Unit = {

  val spark = SparkSession
    .builder()
    .appName("RDD to DataFrame")
    .master("local[*]")
    .getOrCreate()
```


 