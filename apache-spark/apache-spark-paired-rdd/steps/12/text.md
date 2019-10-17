**Step 2:** Next, we shall be using reduceByKey function to sum up all the ratings and all the instances for each userID, by adding together all the rating values and 1's respectively.

```
val totalRatings = mappedRatings.reduceByKey( (x,y) => (x._1 + y._1, x._2 + y._2))
```

The result will be in the form of (userId, (totalRatings, totalInstances))

**Step 3:** Finally, we can now compute the average of the ratings by userId again by using the mapValues function. The average is calculated by dividing totalRatings by totalInstances.

```
val avgRatings = totalRatings.mapValues(x => x._1/x._2)
```
 

We now have the average rating by each user.

