**Step 6:** Instead of using the show method, let us now look how we can save this file. You may comment out or remove the line with the show method from the previous step.

Before we save the file, there is one important thing we need to know about how SparkSQL creates tasks. For the second stage of DAG, the number of tasks created to process the data are 200 by default. But in Spark core, the number of tasks in second stage is always equal to number of tasks in first stage. For example, consider we have two stages stage 0 and stage 1. For stage 0, the number of tasks created will be equal to the number of input splits. Next, in Spark core, the number of tasks in stage 1 are equal to the number of tasks in stage 0. However, in SparkSQL, the number of tasks in stage 1 will be 200 by default.

The 200 tasks in SparkSQL is a good starting point if there is huge data to process. We can configure the number for optimization if required. However, our file is just a sample of small data and there is no requirement of 200 tasks to be created. So using the following property, we can set the total number of tasks as 1. If we run with the default value of 200 and save the file, there will be multiple partitions of output for small set of data. You are free to check how the output looks like without setting this property.
 
```
spark.conf.set("spark.sql.shuffle.partitions", "1")
```

Since this is a configuration, we are calling conf on our SparkSession object and setting the property to use only one task using the set method. This will only create one task and we will be left with only one output file. 

