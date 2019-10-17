
**Step 3:** Let us now run some queries. First, let us run a basic query to select all the users from table who belong to the state Florida.

```
val foridaUsers = spark.sql("SELECT * FROM users WHERE  state = \"FL\"")
```

We use the sql method in our SparkSession object which is spark and enter the following query. We have simply enterd a query to select all the records from our users table who belong to state FL. Since the values of State are String, we have to enclose them in double quotes and use the escape character '\'.

Next, we can simply call show method on floridaUsers dataFrame to check the results.

```
results.floridaUsers.show()
```

Run the program and you should have the result as shown in the screenshot below with the top 20 users who belong to State 'FL'.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 7/Selection_030.png)

To run this program from the terminal, simply run the following command. The program will the then be compiled and executed.
`sbt "runMain training.sqlQueries"`{{execute}} 

You can also use the collect, foreach and print to print all the records as we used to in the previous exercises.
