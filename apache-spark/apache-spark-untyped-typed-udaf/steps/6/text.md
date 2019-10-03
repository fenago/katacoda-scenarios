**Step 4:** Let us finally use the UDAF in our SQL query as shown below.

val average = sparkSession.sql("SELECT userId,  averageUDAF(rating) AS avgRating FROM ratings GROUP BY userId")

Let us check the result using the show method as shown below

average.show()

The following output is shown.


 
We have successfully written a UDAF, registered and used it in the Spark application.

Task 5 is complete!