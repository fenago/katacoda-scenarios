

**Step 2:** Let is now write the RDD to Sequence file format using the saveAsSequenceFile method as shown below.

`seqRDD.saveAsSequenceFile("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/seqOut")`{{execute T1}}

You may run a cat command from another terminal to check if the save was successful, but the file will not be human readable.

**Important:** 
- Commands below will run in **terminal 2** (It will open automatically on executing command). You can also open it by clicking `+` icon and selecting `new terminal`
- Interface will keep switching back to terminal 1 after executing command, you can manually switch by clicking `terminal 2`.

`ls ~/apache-spark/Files/chapter_10/seqOut`{{execute T2}}

`cat ~/apache-spark/Files/chapter_10/seqOut/part*`{{execute T2}}

We know that the save was successful by looking at SEQ at the beginning of the file. We can also see that the key type is of Text and the value type is of IntWritable.

**Step 3:** Let us now read this Sequence file we just saved. Reading Sequence files is a bit different to what we have been doing so far. While reading the Sequence file, we need to specify the key and value data types also.

Enter into the paste mode and execute the following code.
`:paste`{{execute T1}}

**Note:** After pasting following code in the scala terminal, Press  `Ctrl` + `D` to run code.

```val seqData = sc.sequenceFile("/home/scrapbook/tutorial/apache-spark/Files/chapter_10/seqOut/part-00001"
,classOf[org.apache.hadoop.io.Text]
,classOf[org.apache.hadoop.io.IntWritable])```{{execute T1}}
 

Since this is a Hadoop file format, we need to specify the data types in Hadoop. We have specified the Text and IntWritable types as the types for keys and values since our keys are of String and values are of Int.
