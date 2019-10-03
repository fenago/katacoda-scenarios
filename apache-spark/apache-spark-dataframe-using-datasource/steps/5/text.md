
**Step 4:** Let us now load our file using the code as shown below.

```
val users = spark.read
  .format("csv")
  .options(Map("inferSchema" -> "true", "header" -> "true"))
  .load("chapter_7/us-500.csv")
```

We call the read method on our SparkSession object spark, which we created in the previous step and specify the csv as format for our file using the format method. Next, we use a Map object to specify that our input file contains a header and also ask Spark SQL to infer schema. Since Map contains key value pairs, the keys are to specify properties and the values are true for both. Finally, we specify the path of our file using the load method. Please see that we use options method (plural) to specify more than one option using a Map object. If you only want to specify one option, you should use option method (singular). 

 
 