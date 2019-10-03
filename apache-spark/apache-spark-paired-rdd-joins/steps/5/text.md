
**Step 4:** Now let us load both the files using textFile API and also split the fields by comma delimiter. We shall be using the map function to split the fields for every record in the RDDs.

```
def main(args: Array[String]): Unit = {

  Logger.getLogger("Org").setLevel(Level.ERROR)

val sc = new SparkContext("local[*]", "Joins")

val rating = sc.textFile("chapter_5/ratings.csv").map(x => x.split(','))
val movie = sc.textFile("chapter_5/movies.csv").map(x => x.split(','))
```

By splitting the fields, we can refer them individually while creating a paired RDD.

 
