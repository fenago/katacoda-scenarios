**Step 2:** Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `apache-spark/src/main/scala/training/counters.scala` to view scala file.

```
import org.apache.spark._
import org.apache.spark.SparkContext._
import org.apache.log4j._
```

**Step 3:** Now write the main function along with the error log level setting as always.

 
```
def main(args: Array[String]): Unit = {

  Logger.getLogger("Org").setLevel(Level.ERROR)
```

Also, create a SparkContext object and enter the master  as local to use all the cores and the name of the app as Counters.

```
val sc = new SparkContext("local[*]", "Counters")

Your code so far should look like the one in screenshot below.
```
