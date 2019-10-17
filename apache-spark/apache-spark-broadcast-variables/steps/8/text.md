
**Step 6:** Finally, let us use our broadcast variable to look up the name of movie based on its movie Id. We use the '-' symbol to sort in descending order.

```
val sortedMoviesWithNames = sorted.map(x => (broadNames.value(x._1), x._2))
```

We are using the map higher order function to look up the value of the second field from the broadcast variable, which is the movie name and the second field in our sorted RDD, which is the count. We use the value method to get the value in the broadcast variable. The compiler will look up the movie Id with it's movie name and provides us with the name of the movie as first field in the result and count as second field.
 

Let us print out the result to the console.

```
sortedMoviesWithNames.collect.foreach(println)
```

 

