
As a challenge, please find out the second highest salary from each department using the dense_rank function.

**Step 7:** Similarly, let us look at the row_number and percent_rank.

The row_number function as the name suggest provides a row number for each row starting from 1 irrespective of duplicates. The numbers are neither skipped nor are repeated.

```
val rowNumber = row_number().over(window)
employeeDS.select($"*", rowNumber.as("rowNumber")).show()
```

#### Compile and Run
To run this program from the terminal, simply run the following command. The program will the then be compiled and executed.
`sbt "runMain training.window"`{{execute}} 

The following output is shown when we run the program.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 8/Selection_055.png)


The percent_rank calculates the percent rank of a given row based on the following formula. 

```
(rank - 1) / (the number of rows in the window or partition - 1)
```

For example, if the rank of a row is 11 and there are 101 rows in the partition, the rank will be 11-1/101-1 or 10/100 or 0.1. The percent rank ranges from `0` to `1`. The first row will always have a percent rank of 0.

```
val percentRank = percent_rank().over(window)
employeeDS.select($"*", percentRank.as("percentRank")).show()
```

The following output is shown when we run the program.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 8/Selection_056.png)
