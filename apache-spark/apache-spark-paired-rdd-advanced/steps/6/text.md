
**Step 4:** Create a paired RDD as in Task 2 by writing the main function, setting error log level (optional), creating a SparkContext object and loading the file using the textFile API.

```
def main(args: Array[String]): Unit = {

  Logger.getLogger("Org").setLevel(Level.ERROR)

val sc = new SparkContext("local[*]", "Paired RDD Operations")

val data = sc.textFile("chapter_5/tags.csv")
```

Now create an RDD pair by parsing the data RDD using the recordsParser function.

```
val RDDPair = data.map(parseRecords)
```

We now have our paired RDD. Let us use some operations in the next step on our paired RDD in the next step.