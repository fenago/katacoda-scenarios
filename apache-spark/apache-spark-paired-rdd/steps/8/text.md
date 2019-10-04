Let us now write the main function for our program where we create our paired RDD and perform operations over the paired RDD.

**Step 1:** Write the following main function and error log level as shown below.

```
def main(args: Array[String]): Unit = {

  Logger.getLogger("Org").setLevel(Level.ERROR)
```


**Step 2:** Create a SparkContext object as seen in the previous exercise. The master  as local using all the cores and the name of the app as Average ratings by users.

```
val sc = new SparkContext("local[*]", "Friends By First Name")
```

Now that we have the SparkContext object created, let us load our file using the textFile API.

```
val data = sc.textFile("chapter_5/ratings.csv")
```

We now have an RDD loaded.
