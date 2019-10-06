
**Step 3:** Let us now read the file using the hadoopFile API as shown below. This is the old Hadoop API.

`val hadoopData = sc.hadoopFile[Text, Text, KeyValueTextInputFormat]("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/part-r-00000")`{{execute T1}} 

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 10/Selection_025.png)

We now have an RDD from Hadoop MapReduce output. However, in order to access the key value pairs, we have to first convert them to the Java datatypes as we did with the Sequence files.

**Step 4:** Convert the data types from Hadoop types as shown below.

Enter into the paste mode and execute the following code.
`:paste`{{execute T1}}

**Note:** After pasting following code in the scala terminal, Press  `Ctrl` + `D` to run code.

```val hadoopRDD = hadoopData.map
{
	case (x, y) => (x.toString, y.toString)
}```{{execute T1}}

 
![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 10/Selection_026.png) 





