**Step 3:** Write the recordsParser function as in the previous task. For this task, let us extract the movieID and tag fields. The recordsParser function is as shown below.

```
def parseRecords (rows: String): (Int, String)={
val records = rows.split(",")
val movieID = records(1).toInt
val tags = records(2).toString
(movieID, tags)
}
```

