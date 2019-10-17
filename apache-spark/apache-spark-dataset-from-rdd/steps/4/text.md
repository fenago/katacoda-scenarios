**Step 2:** Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `apache-spark/src/main/scala/training/rddToDs.scala` to view scala file.

```
import org.apache.spark.sql.SparkSession
```

**Step 3:** Let us now create a case class so that we can define schema to our dataset as we did with DataFrame in the previous exercise. The names which we specify for attributes of case class object will get mapped as column names for our dataset. 

```
case class Players(player_name: String, team: String, position: String, height: Int, weight: Int, age: Double)
```
