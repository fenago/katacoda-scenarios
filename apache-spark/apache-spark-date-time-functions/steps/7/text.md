

**Step 5:** Next, let us use the timestamp functions. Since we have only created a date type in the previous dataset, let us create a timestamp type instead of date type. First, let us create the dataset and rename the columns as shown below.

Enter into the paste mode and execute the following code.
`:paste`{{execute}}

**Note:** After pasting following code in the scala terminal, Press  `Ctrl` + `D` to run code.

```val timeStamp = spark.createDataset(Seq(
  (1, "Ernesto", "2015-09-24 00:01:12"),
  (2, "Lee", "1985-05-16 03:04:15"),
  (3, "John", "2012-07-16 06:07:18"),
  (4, "Doe", "1914-08-02 09:10:20")
))```{{execute}} 


Enter into the paste mode and execute the following code.
`:paste`{{execute}}

**Note:** After pasting following code in the scala terminal, Press  `Ctrl` + `D` to run code.

```val timeStampDS = timeStamp
  .withColumnRenamed("_1", "id")
  .withColumnRenamed("_2", "name")
  .withColumnRenamed("_3", "timeStamp")```{{execute}} 

Let us print the schema so that we can compare it with the timestamp type in the next step.

`timeStampDS.printSchema()`{{execute}} 



