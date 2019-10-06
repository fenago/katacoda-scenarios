

**Step 4:** Let us now use the arithmetic functions to manipulate the date.

Enter into the paste mode and execute the following code.
`:paste`{{execute}}

**Note:** After pasting following code in the scala terminal, Press  `Ctrl` + `D` to run code.

```val arithmetic = casted
  .withColumn("ageInDays", datediff(current_date(), $"date"))
  .withColumn("addedDays", date_add($"date", 25))
  .withColumn("subtrDays", date_sub($"date", 16))
  .withColumn("addedMonths", add_months($"date", 4))
  .withColumn("lastDay", last_day($"date"))
  .withColumn("nextDay", next_day($"date", "tuesday"))
  .withColumn("monthsBetween", months_between(current_date(), $"date", true))```{{execute}} 


`arithmetic.show()`{{execute}} 

- The datediff function is used to calculate the date difference between two dates. Here we have used the current_date method to get the present date and get the difference from the date in date column.

- The date_add and date_sub functions are used to add and subtract the number of days from the date in date column. The function takes the date column and the number of days  as arguments.


- The add_months function is used to add number of months to the date in date column. The function takes the date column and the number of months  as arguments.

- The last_day and next_day functions are used to get the last day of the month and next day of the month for the day of the week for the date in date column respectively. The next_day function takes date column and the day of week as arguments.

- The months_between function is used to get the number of months between two days. We have used the present date using current_date function and date column as the arguments.



 