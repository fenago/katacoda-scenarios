
**Step 7:** Let us now write some functional style programming using our Dataset. First, we shall extract the two columns userId and rating from the movies dataset using the map function.

```
val users = movies.map(x => (x.userId, x.rating))
```

As you can see, we have used functional style programming the code above which we cannot use with DataFrames. Also, we are able to refer to the column by its name.
 
Next, let us convert our Dataset to RDD and write some code to find out average rating for each user.

```
val count = users.rdd.mapValues(x => (x,1))
  .reduceByKey((x,y) => (x._1 + y._1, x._2 + y._2))
  .mapValues(x => x._1/x._2)
  .sortByKey(false)
```

We have simply used the rdd method to convert our dataset to RDD. The rest of the code is the familiar functional programming style.

Let us now use the collect method as we used to in the previous exercises and print out the result to the console.

```
count.collect.foreach(println)
	}
}
```

 

