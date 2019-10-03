

**Step 4:** We can now use the collect function to collect the final result from the RDD and display it on the console using the following line of code. This action triggers DAG and the job is executed.

avgRatings.collect.foreach(println)

 

**Step 5:** Run the program by clicking on the play icon and Run option as shown in the screenshot below.

 

Once the job is finished, check the output in the console as shown in the screenshot below.

 






 
More Op.

Pair RDD Joins
Pair RDD Actions

 

You can also sort the result by the key by referring the first element in the sortBy function or simply using the sortByKey function key as shown below.

val sorted = avgRatings.sortByKey()
