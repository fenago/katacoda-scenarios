
**Step 3:** The first method is to specify the inputSchema i.e., the data types of input parameters we will be passing for this UDAF.

```
def inputSchema: StructType = StructType(Array(StructField("inputColumn", DoubleType)))
```

The inputSchema method returns a StructType. The inputColumn is of DoubleType as the ratings column is of type Double is enclosed in an array of StructField, which is in turn enclosed in StructType. We are assigning schema to the input by using the StructType and StructField methods as this is a untyped UDAF.

**Step 4:** Next, we have to specify the bufferSchema method. The bufferSchema tells how the data is being aggregated when the tasks are working inside the executors.

To understand this better, consider we have ratings column with four rows as shown below.

**Ratings**
`2.5`
`5.0`
`3.5`
`4.5`

When we perform the average, we first have to compute the sum of all the rows in a column and their count. The sum divided by count gives the average. So, the task which processes the average of rows of the column has to store the intermediate sum and the count of records in a buffer.

The buffer is first initialized as (0, 0) implying the sum and count of ratings respectively. So, the task reads the first row and updates the buffer values as (2.5, 1) by adding the initial values where 2.5 is sum and 1 is the count. Next, when the task reads second row of ratings column, the buffer will update the values as (7.5, 2). The buffer will then be updated as (11.0, 3) for third row and (15.5, 4) for fourth row. Therefore, we need to provide the data type for the count and sum of buffer. We do this using the bufferSchema method as shown below.

```
def bufferSchema = StructType(Array(StructField("sum", DoubleType),StructField("count", LongType)))
```

We are specifying the bufferSchema as we did with the inputSchema using StructType and StructField. The sum is of DoubleType and count is of LongType.
