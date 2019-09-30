Task 4: Implementing Accumulators V2

Please see that this is implementation of Accumulators in Spark 2.x. There will be some code related to dataframes, which we have not covered yet. But worry not. Just look at the implementation of Accumulators V2 and after we cover Dataframes, it all makes sense. 

Step 1: We shall be using the same file we used in the Task 1 for this task as well since we are accumulating the bad records in the input data.


Step 2: Open IDE, right-click the training package which you have created in previous exercise and hover over New and then click on Scala Class. When prompted, enter countersV2 as the name and click on the dropdown for Kind and select Object. Enter the import as shown below.

import org.apache.spark.sql.SparkSession

Since we are working on Spark 2.x, we will have to import a SparkSession object instead if a SparkContext object. The SparkContext object is wrapped within the SparkSession object. The SparkSession objectwill be used to read the data.

 