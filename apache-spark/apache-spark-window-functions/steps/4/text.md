**Step 2:** Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `apache-spark/src/main/scala/training/window.scala` to view scala file.

```
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.expressions.Window
import org.apache.spark.sql.functions._
```

Next, we need to write a case class so that we can specify the schema for our fields. 

```
case class Employee(name: String, number: Int, dept: String, pay: Double, manager: String)
```

We have created a case class and named it Employee by specifying the fields and its types.
