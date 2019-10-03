

**Step 5:** Let us now look at the count of users by state and also arrange them in descending order of their count.

**Note:** You may comment out the previous queries to avoid processing them again.


```
val userCountByState = spark.sql("SELECT state, count(*) AS count FROM users GROUP BY state ORDER BY count DESC)
totalUsersNJ.show()
```

In the query above, we have used GROUP BY to to group by state and then ORDER BY to sort the count in descending order.

The result is as shown in the screenshot below.








