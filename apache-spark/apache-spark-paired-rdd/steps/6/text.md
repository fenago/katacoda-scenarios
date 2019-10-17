**Step 4:** Now, using the split function, we split each field in the record by a comma as we know that each field in our record is separated by comma.

```
val records = rows.split(",")
```

**Step 5:** Now that we have splitted the records, all we have to do is extract the required fields and convert the userId to integer and ratings to float types.

```
val userId = records(0).toInt
val ratings = records(2).toFloat
```

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 5/Selection_011.png)

The records variable contains of 4 fields. We can simply access them based on the index starting from 0. So, we simply extract the userId which is the first field to the variable userId and ratings which is the third field to the variable ratings.
