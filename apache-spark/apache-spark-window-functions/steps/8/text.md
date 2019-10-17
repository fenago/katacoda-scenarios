
**Step 7:** Let us now look at dense_rank. Both these functions are similar and provide the increasing integer value based on the ordering of rows. However, there is a difference when it comes to dealing with duplicate values. If there are two duplicate values, the rank function allocates the same rank for both the rows and skips the next rank for next row and allocates next incremental rank for the next row instead. For example, if rank 1 as allocated to top two rows due to presence of duplicate values, rank 2 will be skipped and instead rank 3 will be allocated to the next row.

However, the dense_rank function doesn't skip the ranks when it encounters duplicate values. In the example above, the dense_rank will alocate same rank i.e., rank 1 for duplicate rows and then rank 2 for the next row. Let us look at this now.

```
val denseRanked = dense_rank().over(window)
```

Let us now call the show method on our dataset and add the rank column using the select function.

```
employeeDS.select($"*", denseRanked.as("dense_rank")).show()
```

The following output is shown when we run the program.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 8/Selection_054.png)

