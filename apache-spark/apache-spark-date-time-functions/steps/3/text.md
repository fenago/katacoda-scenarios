
Let us now look at Date/Time functions to manipulate, extract and perform arithmetic operations on date and time. As in collection functions, we shall be using the Spark shell to demonstrate Date/Time functions as well. 

Fire up the spark-shell from the terminal `spark-shell`{{execute}}


**Step 1:** Let us first create a collection with data as shown below. Please make sure you have the imports from the previous section already imported. You will have to import them again if you have closed the Spark Session.

```val dates = Seq(
  (1, "Ernesto", "2015-09-24"),
  (2, "Lee", "1985-05-16"),
  (3, "John", "2012-07-16"),
  (4, "Doe", "1914-08-02"))```{{execute}} 


Next, let us convert the collection to dataset using the toDS method and rename the column as shown below using the withColumnRenamed method. The default column names for dataset are monotonically increasing numbers like _1, _2, _3 etc.

`val datesDS = dates.toDS().withColumnRenamed("_1", "id").withColumnRenamed("_2", "name").withColumnRenamed("_3", "date")`{{execute}} 


Let us check the schema using the printSchema method, so that we can compare the datatype for date column in the next step.

`datesDS.printSchema()`{{execute}} 

As you can see, the date is of type String.
