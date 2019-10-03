

**Step 5:** Now let is write a foreach statement to take each record from the input data, split the records by a comma and test it against a condition. If the records do not contain four fields, we increment the badRecords variable by one using the add method as shown below.

Since we know that our records contain 4 fields and if there are less than four fields in a record, we treat it as a bad record.

```
data.foreach(record => {
  val fields = record.split(",")

  if (fields.size != 4)
	badRecords.add(1)
})
```

 

