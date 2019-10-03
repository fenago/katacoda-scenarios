**Step 2:** Open IDE, right-click the training package which you have created in previous exercise and hover over New and then click on Scala Class. When prompted, enter counters as the name and click on the dropdown for Kind and select Object. Enter the imports as shown below.

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
