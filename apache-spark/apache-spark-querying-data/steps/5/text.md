
**Step 1:** We shall be using the file `us-500.csv`, for this task as input source. Please create a new object and name it sqlQueries. Perform all the steps you performed in Task 1 and come back here. Your program should look something like the screenshot shown below.



**Step 2:** Let us first assign a view for our dataFrame so that we can run queries against it. In simple words, we are just creating a table for our dataFrame so that we can reference it while we run SQL queries against it. 

```
users.createOrReplaceTempView("users")
```

We are using the createOrReplaceTempView method to create a temporary table named users if it doesn't exist, or replace a view if it already exist with the same name. This temporary table is available till the SparkSession is active. Once the session ends, the table will not be available anymore. Hence the name temp view. You can also persist the table using saveAsTable method.


