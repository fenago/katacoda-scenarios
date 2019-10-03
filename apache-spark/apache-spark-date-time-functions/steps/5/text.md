
**Step 3:** Let us now extract the indivudual attributes from the date object such as day, month, year etc. We shall be using various functions to add columns for each function using the withColumn method.

val extracted = casted
  .withColumn("year", year($"date"))
  .withColumn("month", month($"date"))
  .withColumn("dayOfYear", dayofyear($"date"))
  .withColumn("quarter", quarter($"date"))
  .withColumn("weekOfYear", weekofyear($"date"))

 

We have used the year, month and dayofyear functions to extract the extract the individual attributes from the date column. We have also used the quarter function to get which quarter the date is from and weekofyear function to get the week of which the date belongs to.

The following output is shown when we use the show method.

extracted.show()

 