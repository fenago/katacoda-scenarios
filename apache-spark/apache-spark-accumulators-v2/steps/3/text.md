Task 4: Implementing Accumulators V2

Please see that this is implementation of Accumulators in Spark 2.x. There will be some code related to dataframes, which we have not covered yet. But worry not. Just look at the implementation of Accumulators V2 and after we cover Dataframes, it all makes sense. 

**Step 1:** We shall be using the same file we used in the Task 1 for this task as well since we are accumulating the bad records in the input data.

**Step 2:** Click **IDE Editor** tab to open Visual Studio and open solution explorer and open `apache-spark/src/main/scala/training/countersV2.scala` to view scala file.

```
import org.apache.spark.sql.SparkSession
```

Since we are working on Spark 2.x, we will have to import a SparkSession object instead if a SparkContext object. The SparkContext object is wrapped within the SparkSession object. The SparkSession objectwill be used to read the data.

 