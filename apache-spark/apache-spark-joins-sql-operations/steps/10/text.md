
**Step 4:** Let us now write some code to get the count for all the users for each state. We first need to import the implicits as shown below.

import spark.implicits._

val userCountByState = users.groupBy("state")
    .agg(("state", "count"))
    .orderBy($"count(state".desc)

As you can see in the query above, we use the orderBy method to order the result by the count of state in a descending order.

Let us call the show method.

userCountByState.show()

 

The output is as shown in the screenshot below.


 

Task is complete!



SUMMARY

In this chapter we have looked at basics of Spark SQL. We have learned what is Spark SQL, why it is required and it's architecture in detail.
In the labs, we have had our hands on creating a dataFrame, converting an RDD to dataFrame using the toDF method and StructType. We have then used SQL queries and dataFrame API to process data.
