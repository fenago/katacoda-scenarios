
**Step 4:** Let us now use explode function. The explode function takes each element in the collection and generates a new row. 

```
val exploded = numDS.select($"numbers", explode($"numbers").as("exploded"))
```

In the code above, we have used the select method to select the numbers column, and then the result of using explode function on numbers column as second column. We have specified the second column name as exploded.

After running the show method, the following result is shown as in the screenshot.

```
exploded.show()
```

As you can see from the output, each element inside the collection is a new row.

Similarly, we also have posexplode function, which also provides us with the position of each row.

```
val posExploded = numDS.select(posexplode($"numbers"))
```

When posexplode function is used, two columns are created. One is the column with exploded values as seen above and the other is with the position of each exploded value.

After running the show method, the following result is shown as in the screenshot.

```
posExploded.show()
```

Since we haven't used the as method to specify the names of the columns, the default column names pos and col are created for us.
