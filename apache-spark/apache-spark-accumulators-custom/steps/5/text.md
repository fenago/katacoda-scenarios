
 

**Step 4:** Let us now declare a private HashMap variable called movieCount which will hold the final count of our CountByMovie Accumulator.

```
private val movieCount = new HashMap[Int, Int]()
```

We have to implement a reset method available in the AccumulatorV2 class to reset the accumulator value to zero.

```
def reset() = {
  movieCount.clear()
}
```
 

**Step 5:** We now have to implement the add method to specify the aggregation logic for local accumulators, i.e., the tasks which run on executors. All the tasks running on executors will run the method to aggregate data locally.
 

```
def add(tuple: (Int, Int)): Unit = {
  val movieId = tuple._1
  val updatedCount = tuple._2 + movieCount.getOrElse (movieId, 0)

  movieCount += ((movieId, updatedCount))
}
```

The add method takes two arguments as key and value. The key, which is the first argument, is the movieId, and the second argument, the count of the movieId, is value. We simply extract them into their respective variables and add them to the movieCount Hashmap. The getOrElse method is used to get the value of count if it exists or set a value for that movie as zero and add them with the current count and previous count to get the updated count.

 