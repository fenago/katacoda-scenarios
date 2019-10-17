

**Step 3:** Let us now write our main function, create a SparkContext object and declare our broadcast variable.

```
def main(args: Array[String]): Unit = {


  val sc = new SparkContext("local[*]", "Ratings By movie ")

  val broadNames = sc.broadcast(loadMovieNames)
```

We can create a broadcast variable by simply calling the broadcast method on our SparkContext object. We then pass our loadMovieNames function as parameter to the broadcast method since loadMovieNames function returns a Map object, we will have the Map object broadcasted to all the nodes of the cluster.


**Step 4:** Let us now load our ratings.csv file and create an RDD. Next, we split the records based on comma and extract the movieId field. We then use the map function to create a pairedRDD of movie Id and its count by  1, so that we can count the number of times each movies is rated in the next step.

```
val data = sc.textFile("chapter_6/ratings.csv")
val records = data.map(x => (x.split(",")(1).toInt, 1))
```
