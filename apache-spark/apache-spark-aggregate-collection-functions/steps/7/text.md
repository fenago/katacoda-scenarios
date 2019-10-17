So far, We have been working with IDE and learned how to create objects and run the programs. However, for this task where we learn about collection functions, let us work with the Spark shell so that we can quickly check the output on the fly, instead of running the program everytime we use a function. You may choose to work with IDE and it is perfectly fine. You will then have to create the SparkSession object and specify the required imports.

**Step 1:**  Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `apache-spark/src/main/scala/training/collections.scala` to view scala file.

**Step 2:** We need to import the implicits and functions to be able to work with the functions.

```
import spark.implicits._
import org.apache.spark.sql.functions._
```

Let us now declare a Seq collection as shown below.

```
val num = Seq(Seq(1,2,3), Seq(4, 5, 6), Seq(7,8,9))
```


 