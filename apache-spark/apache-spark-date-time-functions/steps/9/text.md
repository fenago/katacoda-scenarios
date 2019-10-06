
**Step 7:** Let us now extract the attributes from timestamp column as we did for the date column couple of steps ago.

Enter into the paste mode and execute the following code.
`:paste`{{execute}}

**Note:** After pasting following code in the scala terminal, Press  `Ctrl` + `D` to run code.

```val extractedTs = timeStampDS
  .withColumn("second", second($"timeStamp"))
  .withColumn("minute", minute($"timeStamp"))
  .withColumn("hour", hour($"timeStamp"))```{{execute}} 

The output is shown when we use the show method.

`extractedTs.show()`{{execute}} 


 
