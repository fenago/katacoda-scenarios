
**Step 8:** Finally, let us use couple of conversion functions to convert the dates into different formats.

Enter into the paste mode and execute the following code.
`:paste`{{execute}}

**Note:** After pasting following code in the scala terminal, Press  `Ctrl` + `D` to run code.

```val conversions = timeStampDS
    .withColumn("unixTime", unix_timestamp($"timeStamp"))
    .withColumn("fromUnix", from_unixtime($"unixTime"))```{{execute}} 

- The unix_timestamp function is used to convert the timestamp to unix timestamp.

- The from_unixtime function is used to cconvert the unix time which we obtained above.

The output is shown when we use the show method.

`conversions.show()`{{execute}} 


 

Task is complete!

