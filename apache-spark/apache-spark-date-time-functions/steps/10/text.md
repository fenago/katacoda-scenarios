
**Step 8:** Finally, let us use couple of conversion functions to convert the dates into different formats.

val conversions = timeStampDS
    .withColumn("unixTime", unix_timestamp($"timeStamp"))
    .withColumn("fromUnix", from_unixtime($"unixTime"))

●	The unix_timestamp function is used to convert the timestamp to unix timestamp.

●	The from_unixtime function is used to cconvert the unix time which we obtained above.

The following output is shown when we use the show method.

conversions.show()


 

Task 4 is complete!
