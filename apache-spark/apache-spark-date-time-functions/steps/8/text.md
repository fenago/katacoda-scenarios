
Step 6: Let us now convert the timestamp which is of String type to timestamp type.

val castedTimeStamp = timeStampDS.select($"id", $"name", $"timeStamp".cast("timestamp")).cache()

Let us now print the schema and the dataset to check the casting.

castedTimeStamp.printSchema()
castedTimeStamp.show()

As you can see from the screenshot below, we have successfully casted the timestamp column from String type to timestamp type. 


