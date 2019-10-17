
**Step 5:** Let us simply print the file names by using the keys method on textFiles RDD as shown below.

`textFiles.keys.collect.foreach(println)`{{execute T1}} 

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 10/Selection_005.png)

We can also get the values by using the values method. We can also perform all the operations which you can apply on paired RDDs such as mapValues, reduceByKey, sortByKey etc.

This paired RDD can again be saved to filesystem using the saveAsTextFile method as usual.

Let us now use text files with the DataSource API.
