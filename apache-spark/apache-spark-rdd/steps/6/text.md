We can also create an RDD from data present in Hadoop Distributed File System (HDFS) using the same textFile API. But instead of local path, we have to provide a HDFS path.

```
val ratings = sc.textFile("hdfs://dev_server:9000/file.txt")
```

The RDD will be created using the data from HDFS and then you can continue to apply transformations and actions.

Task is complete!

