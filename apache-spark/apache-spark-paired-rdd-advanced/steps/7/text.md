Step 5: Now that we have our paired RDD, let us group all the tags by movieID using the groupByKey function.

val grouped = RDDPair.groupByKey()

 

Let us now print out the result of grouped RDD to the console.


grouped.collect.foreach(println)

The output is as shown in the screenshot below with all the tags for a movie are grouped together.



You may optionally convert the values from compactBuffer to a list by simply mapping the output and converting them to a List as shown below.