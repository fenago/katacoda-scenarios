
**Step 3:** Let us call the show method and run the program.

```
agg.show()
```

The following result should be shown.

**Step 4:** As we can see from the screenshot above, the column names are not so nice. We can assign our own column names using the as method.

```
val aggAlias = movies.select(
  avg("rating").as("avgRating")
  , min("userId").as("lowestUserId")
  , max("movieId").as("highestMovieId")
  , sum("userId").as("sumOfUserId")
  , mean("rating").as("meanRating")
)
```

All we are doing is assigning an alias (column name) to each and every field using the as method.



 