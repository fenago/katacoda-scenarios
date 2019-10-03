
**Step 4:** Let us now write the main function for our program and create a SparkSession object as shown below.

```
def main(args: Array[String]): Unit = {

  val spark = SparkSession
    .builder()
    .appName("RDD to Dataset")
    .master("local[*]")
    .getOrCreate()
```

**Step 5:** Since our aim is to convert an RDD to a Dataset, we must use the textFile API in the SparkContext object to read the file and create an RDD.

```
val input = ss.sparkContext.textFile("chapter_8/mlb_players.csv")
```

We now have an RDD created. But the file contains a header with column names. We must first remove the header. Instead of using the first method and then the filter method, let us remove the header using an efficient approach.

```
val removeHeader = input.mapPartitionsWithIndex((index, itr) => {
  if (index == 0) itr.drop(1) else itr
})
```

In the previous approach to remove the header, we were using filter method to filter out the first record from the RDD. This approach works well when there is small data. But, Spark isn't developed for small data. We will be using huge data in realtime environment.

Consider a scenario where we have a billion records in our RDD. When we use the filter function, the filter condition is tested for each and every record of RDD. Just to filter out one record, we end up testing the condition for all the billion records. To overcome this, we can use the mapPartitionWithIndex function. This higher order function provides us with an entire partition of RDD with index unlike map function which provides us with each record. We can then pass our logic which is to drop the first record in the partition if the partition index is 0, else return the partition as is. So, the condition inside if statement is only verified per partition basis instead of per record. This condition is only tested based on the number of partitions and not on the number of records making it efficient.
 

 