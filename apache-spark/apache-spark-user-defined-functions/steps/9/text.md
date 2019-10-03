
**Step 7:** Let us now register this new UDF by using the partially applied function as shown below. We have used the underscore placeholder to specify that this is a partially applied function for which the parameter will be passed later in the program.

spark.udf.register("decrUDF2", decrUDF2 _)

Let us also create a temporary table using createOrReplaceTempView function as shown below. We can then run our SQL queries over this table.

ratings.createOrReplaceTempView("ratings")

val ratingDecDf = spark.sql("select *, decrUDF2(rating) as ratingDec from ratings")

The program should look something like the screenshot shown below.


 

**Step 8:** Let us finally call the show method and check the output.

ratingDecDf.show()

The following output is shown.

 
With this we have written, registered and use a UDF.

Task is complete!




