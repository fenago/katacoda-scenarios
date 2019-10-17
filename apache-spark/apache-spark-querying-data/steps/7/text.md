
**Step 4:** Let us now run a query to check the count of total users who belong to state "New Jersey".

```
val totalUsersNJ = spark.sql("SELECT count(*) AS NJ_Count FROM users WHERE state = \"NJ\"")
totalUsersNJ.show()
```

**Important:** You need to uncomment above line in `sqlQueries.scala` using **vscode** editor before running program again.

`sbt "runMain training.sqlQueries"`{{execute}} 

In the query above, we are simply using count function with a WHERE clause to get the count of users who belong to NJ. We use the AS clause to name the column as shown in the screenshot below. Then, we use the show method to display the results.

The output should be as shown in the screenshot below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 7/Selection_031.png)



