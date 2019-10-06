**Step 6:** Instead of using the show method, let us now look how we can save this file. You may comment out or remove the line with the show method from the previous step.

Before we save the file, there is one important thing we need to know about how SparkSQL creates tasks. For the second stage of DAG, the number of tasks created to process the data are 200 by default. But in Spark core, the number of tasks in second stage is always equal to number of tasks in first stage. For example, consider we have two stages stage 0 and stage 1. For stage 0, the number of tasks created will be equal to the number of input splits. Next, in Spark core, the number of tasks in stage 1 are equal to the number of tasks in stage 0. However, in SparkSQL, the number of tasks in stage 1 will be 200 by default.

The 200 tasks in SparkSQL is a good starting point if there is huge data to process. We can configure the number for optimization if required. However, our file is just a sample of small data and there is no requirement of 200 tasks to be created. So using the following property, we can set the total number of tasks as 1. If we run with the default value of 200 and save the file, there will be multiple partitions of output for small set of data. You are free to check how the output looks like without setting this property.
 
```
spark.conf.set("spark.sql.shuffle.partitions", "1")
```

Since this is a configuration, we are calling conf on our SparkSession object and setting the property to use only one task using the set method. This will only create one task and we will be left with only one output file. 

#### Save File
Let us now save the file using the code below.

```
 userCountByState.write
    .format("csv")
    .save("chapter_7/output")
```

Similar to reading the file using read and load methods, we use write and save methods to save the file to file system.

 

Now run the program as you did in the previous task and check the output directory. You should see two files: part-00000 and a _SUCCESS file. The output is saved in part-00000 file.
 
`sbt "runMain training.sqlQueries"`{{execute}} 

#### Output Files

`ls ~/apache-spark/chapter_7/output`{{execute}} 

`cat ~/apache-spark/chapter_4/word_count/output/part-00000*`{{copy}} 

Open the `part-00000-<guid>` file and you should see the result as shown below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 7/Selection_034.png)

This way you can perform any operations using the SQL data manipulation language. 

Task is complete!


