
**Step 2:** Now that we have the dataFrame created, let us perform an operation to select all the users from Florida using the DataFrame API.

```
val foridaUsers = users.select("*").where("state = \"FL\"")
```

This is similar to the SQL query which we have performed in the task earlier. We have methods here which look more like programming style. In the code above, we have used select method to select all the columns of out dataFrame and then where method to specify our condition.

Please see that we need not create a temp view as we did earlier. It is only required when we are working with SQL queries.

Let us now call the show method on our dataFrame to view the results on the console.

```
floridaUsers.show()
```

The output should look something like the table shown in the screenshot.

 