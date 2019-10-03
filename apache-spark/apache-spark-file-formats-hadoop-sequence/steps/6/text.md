
**Step 4:** However, since these are Hadoop data types, we cannot access the keys directly. We need to convert them to Java data types as shown below. The job will fail if we do not convert the data types and collect.

scala> val newRDD = seqData.map
{
	case (x, y) => (x.toString, y.get())
}
  

As you can see from the screenshot above, we now have the RDD[(String, Int)]. We can now simply perform all the operations we usually do on RDDs. We have to use the toString method when converting from Hadoop’s Text type and the get method for other data types.

**Step 5:** Let us now collect the RDD and check out the results.

scala> newRDD.collect()

 

With this we have successfully written and read the Sequence files.