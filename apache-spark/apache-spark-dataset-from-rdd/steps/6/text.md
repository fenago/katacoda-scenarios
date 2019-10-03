

**Step 6:** The next step is similar to what we have done in the previous exercise while creating a DataFrame from RDD. We split the fields based on a comma so that we can assign each individual field to its appropriate case class field.

```
val fields = removeHeader.map(record => record.split(","))
```

Now that we can access individual fields by their position, let us assign them to the case class Players, using the map function as shown below.

```
val structRecords = fields.map(field => Players(field(0).trim, field(1).trim, field(2).trim, field(3).trim.toInt, field(4).trim.toInt, field(5).trim.toDouble))
```

We call trim method on all the fields to remove leading and trailing white spaces, and also cast height, weight and age fields to Int, Int and Double respectively.

 