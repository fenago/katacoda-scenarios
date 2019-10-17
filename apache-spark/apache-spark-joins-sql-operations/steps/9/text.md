

**Step 3:** Let us now run a query to check the count of total users who belong to state "New York".
 
```
val nyUserCount = users.groupBy("state")
    .agg(("state", "count"))
    .where("state = \"NY\"")
```

This is a bit different to what we have done in the SQL query. In the code above, we are first grouping by state and then applying the agg method. The agg method takes the column as first parameter and then the type of aggregation as second parameter. We specify the second parameter as count since we want to count the number of users from New York State. Then, we specify the condition using the where method.

Let us now call the show method on our dataFrame to view the results.

```
nyUserCount.show()
```

The output is as shown in the screenshot below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 7/Selection_044.png)

 

