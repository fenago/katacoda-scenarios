

**Step 5:** Now that we have both the datasets loaded and splitted by comma delimiter, let us create a tuple of two elements (Paired RDD) so that we can perform a join on both the RDDs based on key. The key here will be the movieID.

To create a tuple, we use the map function with the first element (key) of the tuple as movieID which is second field in the rating RDD and first field in movie RDD. The second element (value) of the tuple will be the entire records from both the RDDs.

```
val rating_record = rating.map(x => (x(1).toInt, ratings(x(0).toInt, x(1).toInt, x(2).toFloat, x(3).toString)))

val movie_record = movie.map(x => (x(0).toInt, movies(x(0).toInt, x(1).toString, x(2).toString)))
```

**Step 6:** The next step is to simply perform the join as shown below.

```
val joined = rating_record.join(movie_record)
```

Now we can simply collect the results and print them to the console.

```
joined.collect.foreach(println)
```

The output with the joined results can be seen as shown in the screenshot below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 5/Selection_038.png)

You can then similarly perform the rest of the joins such as left outer join and right outer join.

It is recommended to perform joins using dataframes rather than RDDs as it can have the benefit of catalyst optimizer when performed using dataframes. We shall look at dataframes in our upcoming scenarios.

Task is complete!

