
**Step 2:** Let us first use the countByKey function to check the number of ratings per movie on our joined RDD.

```
val count = joined.countByKey()
```

Let us print the count to the console using the println function and run the program. You should see the result as shown below with count of reviews for each movie is shown as a Map collection.

```
println(count)
```

**Step 3:** Let us now use the collectAsMap function on the joined RDD.

```
val mappedCol = joined.collectAsMap()
println(mappedCol)
```

The result is returned as a Map collection with all the duplicate keys removed.

 




