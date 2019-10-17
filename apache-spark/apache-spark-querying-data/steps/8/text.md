

**Step 5:** Let us now look at the count of users by state and also arrange them in descending order of their count.

```
val userCountByState = spark.sql("SELECT state, count(*) AS count FROM users GROUP BY state ORDER BY count DESC)
userCountByState.show()
```

**Important:** You need to uncomment above line in `sqlQueries.scala` using **vscode** editor before running program again.

`sbt "runMain training.sqlQueries"`{{execute}} 

In the query above, we have used GROUP BY to to group by state and then ORDER BY to sort the count in descending order.

The result is as shown in the screenshot below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 7/Selection_032.png)








