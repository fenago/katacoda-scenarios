
**Step 2:** Open IDE, right-click the training package which you have created in previous exercise and hover over New and then click on Scala Class. When prompted, enter users as the name and click on the dropdown for Kind and select Object. Enter the import as shown below.

```
import org.apache.spark.sql.SparkSession
```

Since we are using SparkSession object to start our Spark Session, we need not import the SparkContext object as we did in the previous exercises. The SparkContext object is wrapped with in the SparkSession object in Spark 2.x version.


**Step 3:** Let us now write the main function for our program and create a SparkSession object as shown below.

```
def main(args: Array[String]): Unit = {

  val spark = SparkSession
    .builder()
    .appName("Users")
    .master("local[*]")
    .getOrCreate()
```

We are calling the builder method on Sparksession object to build a Spark Session. Next, the appName and master methods are used to specify the name of our app and mode of execution (local or cluster), as we used to while creating a SparkContext object. Finally, we use the getOrCreate method to get a SparkSession if there is one already or create a new SparkSession if it does not exist.

 
