
Step 3: Let us now read the file using the hadoopFile API as shown below. This is the old Hadoop API.

scala> val hadoopData = sc.hadoopFile[Text, IntWritable, KeyValueTextInputFormat](“/IdeaProjects/Spark/chapter_10/part-r-00000”)

 

We now have an RDD from Hadoop MapReduce output. However, in order to access the key value pairs, we have to first convert them to the Java datatypes as we did with the Sequence files.

Step 4: Convert the data types from Hadoop types as shown below.

scala> val hadoopRDD = hadoopData.map
{
	case (x, y) => (x.toString, y.toString)
}

 





