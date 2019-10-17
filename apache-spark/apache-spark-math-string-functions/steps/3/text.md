There are a number of math functions which can be applied to columns with numbers. Let us now look at few of them.

Fire up the spark-shell from the terminal `spark-shell`{{execute}}

**Step 1:** Let us first create a collection with data as shown below. Please make sure you have the imports from the previous section already imported. You will have to import them again if you have closed the Spark Session.

`val numbers = List(5, 4, 9.4, 25, 8, 7.7, 6, 52)`{{execute}} 

**Step 2:** Next, let us convert the collection to dataset using the toDS method and rename the column as numbers using the withColumnRenamed method. The default column name when you create a dataset is value. Hence we change the default column name to numbers.

```val numbersDS = numbers.toDS().withColumnRenamed("value", "numbers").cache()```{{execute}} 

The dataset should now be created with the renamed column.

 
