

**Step 5:** Since our aim is to convert an RDD to a DataFrame, we must use the textFile API in the SparkContext object to read the file and create an RDD.

```
val input = ss.sparkContext.textFile("chapter_7/mlb_players.csv")
```

We now have an RDD created. But the file contains a header with column names. We must first remove the header. We can achieve that by calling the first method on our RDD and then remove it using the filter method as shown below.

```
val header = input.first()
val records = input.filter(x => x != header)
```

The first line of code takes the first record from the RDD, which in our case is the header or column names and then we simply filter out the header from input RDD. Now, we just have the records RDD without the column names.


**Step 6:** The next step is to split the fields based on a comma so that we can assign each indivudual field to its appropriate case class field.

```
val fields = records.map(record => record.split(","))
```

Now that we can access indivudual fields by their position, let us assign them to the case class Players, using the map function as shown below.

```
val structRecords = fields.map(field => Players(field(0).trim, field(1).trim, field(2).trim, field(3).trim.toInt, field(4).trim.toInt, field(5).trim.toDouble))
```

We call trim method on all the fields to remove leading and trailing white spaces, and also cast height, weight and age fields to Int, Int and Double respectively.





