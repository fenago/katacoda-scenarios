Let us now work with Hadoop and Sequence Files. These files are popular file formats with Hadoop MapReduce framework. These files contains key value pairs in binary format. Let us first create and write a Sequence file and then read the same sequence file.

Open the terminal and fire up the Spark shell `spark-shell`{{execute T1}}

#### Sequence Files
**Step 1:** Let us first create an RDD using the parallelize method as shown below.

`val seqRDD = sc.parallelize(List(("Ernesto", 2000), ("Learning", 4500), ("Lee", 8000)))`{{execute T1}}

This will create and RDD[(String, Int)] as shown below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 10/Selection_019.png)
 