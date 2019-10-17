
**Step 4:** Let us now write some code to get the count for all the users for each state. We first need to import the implicits as shown below.

```
import spark.implicits._

val userCountByState = users.groupBy("state")
    .agg(("state", "count"))
    .orderBy($"count(state".desc)
```

As you can see in the query above, we use the orderBy method to order the result by the count of state in a descending order.

Let us call the show method.

```
userCountByState.show()
```

To run this program from the terminal, simply run the following command. The program will the then be compiled and executed.
`sbt "runMain training.dfOps"`{{execute}} 

The output is as shown in the screenshot below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 7/Selection_047.png)
 
Task is complete!
