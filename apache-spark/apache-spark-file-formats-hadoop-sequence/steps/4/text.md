Task 6: Hadoop and Sequence Files

Let us now work with Hadoop and Sequence Files. These files are popular file formats with Hadoop MapReduce framework. These files contains key value pairs in binary format. Let us first create and write a Sequence file and then read the same sequence file.



Sequence Files
**Step 1:** Let us first create an RDD using the parallelize method as shown below.

scala> val seqRDD = sc.parallelize(List((“Ernesto”, 2000), (“Learning”, 4500), (“Lee”, “8000”)))
 
This will create and RDD[(String, Int)] as shown below.

 