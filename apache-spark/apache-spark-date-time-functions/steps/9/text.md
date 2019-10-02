
Step 7: Let us now extract the attributes from timestamp column as we did for the date column couple of steps ago.

val extractedTs = timeStampDS
  .withColumn("second", second($"timeStamp"))
  .withColumn("minute", minute($"timeStamp"))
  .withColumn("hour", hour($"timeStamp"))

The functions used above are self explanatory.

The following output is shown when we use the show method.

extractedTs.show()


 
