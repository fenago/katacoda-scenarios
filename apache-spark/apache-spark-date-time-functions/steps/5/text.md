
**Step 3:** Let us now extract the indivudual attributes from the date object such as day, month, year etc. We shall be using various functions to add columns for each function using the withColumn method.

Enter into the paste mode and execute the following code.
`:paste`{{execute}}

**Note:** After pasting following code in the scala terminal, Press  `Ctrl` + `D` to run code.

```val extracted = casted
  .withColumn("year", year($"date"))
  .withColumn("month", month($"date"))
  .withColumn("dayOfYear", dayofyear($"date"))
  .withColumn("quarter", quarter($"date"))
  .withColumn("weekOfYear", weekofyear($"date"))```{{execute}} 

#### Output
We have used the year, month and dayofyear functions to extract the extract the individual attributes from the date column. We have also used the quarter function to get which quarter the date is from and weekofyear function to get the week of which the date belongs to.

`extracted.show()`{{execute}} 