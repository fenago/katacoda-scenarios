

**Step 5:** Now that we have a pairedRDD, we can use the reduceByKey function to count the number of of times each movie has been rated as shown below.

```
val count = records.reduceByKey((x,y) => x + y)
```

Let us now sort the count i.e., second field in desceinding order so that the highest number of rated movie will be on the top of our result.

```
val sorted = count.sortBy(-_._2)
```

 
