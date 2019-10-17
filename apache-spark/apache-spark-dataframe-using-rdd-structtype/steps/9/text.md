
**Step 4:** Now, instead of mapping the fields to a case class as in previous task, we map the fields to a Row object. This Row object is an ordered collection of fields, which can be accessed by index or position. It is similar to a row in a table.

```
val structRecords = fields.map(field => Row(field(0).trim, field(1).trim, field(2).trim, field(3).trim.toInt, field(4).trim.toInt, field(5).trim.toDouble))
```

We now have our fields as rows. All the fields are assigned and casted as we have in the previous task.

**Step 5:** Now that we have rows, let us create a schema. We can create schema using the instance of StructType object. The StructType object contains StructField objects which takes parameters as name of the column, type of the column and an optional boolean specifying if the column contains null values. Also, the data type must be defined as StringType, IntegerType, DoubleType etc.

```
val schema = StructType(List(
  StructField("player_name", StringType, false),
  StructField("team", StringType, false),
  StructField("position", StringType, false),
  StructField("height", IntegerType, false),
  StructField("weight", IntegerType, false),
  StructField("age", DoubleType, false)
))
```

We have specified the StructFields as a List inside the StructType object.
