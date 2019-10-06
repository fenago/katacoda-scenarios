
**Step 6:** Let us now convert the timestamp which is of String type to timestamp type.

`val castedTimeStamp = timeStampDS.select($"id", $"name", $"timeStamp".cast("timestamp")).cache()`{{execute}} 

Let us now print the schema and the dataset to check the casting.

```castedTimeStamp.printSchema()
castedTimeStamp.show()```{{execute}} 

As you can see, we have successfully casted the timestamp column from String type to timestamp type. 


