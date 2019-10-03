
As a challenge, please find out the second highest salary from each department using the dense_rank function.

**Step 7:** Similarly, let us look at the row_number and percent_rank.

The row_number function as the name suggest provides a row number for each row starting from 1 irrespective of duplicates. The numbers are neither skipped nor are repeated.

val rowNumber = row_number().over(window)
employeeDS.select($"*", rowNumber.as("rowNumber")).show()

The following output is shown when we run the program.

 

The percent_rank calculates the percent rank of a given row based on the following formula. 

(rank - 1) / (the number of rows in the window or partition - 1)

For example, if the rank of a row is 11 and there are 101 rows in the partition, the rank will be 11-1/101-1 or 10/100 or 0.1. The percent rank ranges from 0 to 1. The first row will always have a percent rank of 0.

val percentRank = percent_rank().over(window)
employeeDS.select($"*", percentRank.as("percentRank")).show()

The following output is shown when we run the program.

 

**Step 8:** Let us finally look at lead and lag functions. The lead and lag functions are used to find how much the value of next row is leading or lagging when compared to the current row.

val leads = lead($"pay", 1, 0).over(window)
employeeDS.select($"*", leads.as("lead")).show()

The lead function takes three arguments. The first is the column name, second is the offset value, which determines the number of rows preceding/succeeding the current row and the third is the default to specify the default value if the offset is outside the scope of the window.

The following output is shown when we run the program.

 

Similarly, there is lag function which calculates the lag.

val lags = lag($"pay", 1, 0).over(window)
employeeDS.select($"*", lags.as("lag")).show()

The following output is shown when we run the program.

 

Task 6 is complete!



