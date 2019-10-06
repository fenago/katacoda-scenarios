

**Step 2:** Let is now write the RDD to Sequence file format using the saveAsSequenceFile method as shown below.

`seqRDD.saveAsSequenceFile("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/seqOut")`{{execute T1}}

You may run a cat command from another terminal to check if the save was successful, but the file will not be human readable as shown in the screenshot below.

`cat /home/scrapbook/tutorial/apache-spark/Files/chapter_10/seqOut/part*`{{execute T1}}

 
 
We know that the save was successful by looking at SEQ at the beginning of the file. We can also see that the key type is of Text and the value type is of IntWritable.

**Step 3:** Let us now read this Sequence file we just saved. Reading Sequence files is a bit different to what we have been doing so far. While reading the Sequence file, we need to specify the key and value data types also.

```val seqData = sc
.SequenceFile("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/seqOut/part-00000"
,classOf[org.apache.hadoop.io.Text]
,classOf[org.apache.hadoop.io.IntWritable])```{{execute T1}}
 

Since this is a Hadoop file format, we need to specify the data types in Hadoop. We have specified the Text and IntWritable types as the types for keys and values since our keys are of String and values are of Int.
