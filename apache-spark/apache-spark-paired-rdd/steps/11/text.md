**Step 1:** At this point, we have a paired RDD with userId as key and ratings as value. We now have to compute the sum of user ratings and divide them by the number of ratings so that we can get the average rating by an user.

To achieve this, we must first compute the number of ratings by an user using the mapValues function. 

```
val mappedRatings = RDDPair.mapValues(x => (x,1))
```

This transformation converts each rating value to a tuple of (ratings, 1). So we will be having our Paired RDD as (userId, (ratings, 1)).

You may optionally print out the mappedRatings to the console, to check how the result is displayed.
