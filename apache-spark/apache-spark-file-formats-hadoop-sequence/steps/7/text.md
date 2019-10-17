We can also read the output of Hadoop MapReduce jobs to Spark using the hadoopFile and newAPIHadoopFile methods. The hadoopFile method is the old Hadoop API while newAPIHadoopFile method is the new Hadoop API.

The syntax to read a Hadoop file using the old Hadoop API is as follows.

```
sparkContext.hadoopFile[keyDataType, valueDataType, inputFormatClass]("/path/to/file")
```

As you can see from the syntax above we have to specify the data types of both keys and values and also the Hadoop input format class for the input file.

An example of this is as follows.

```
sparkContext.hadoopFile[Text, LongWritable, TextInputFormat]("/usr/local/files/out/part-00000")
```
Please note that we should import the required classes for data types and input formats as required. 

The syntax to read a Hadoop file using the new Hadoop API is as follows.

```
sparkContext.newAPIHadoopFile("/path/to/file", classOf[inputFormatClass], classOf[keyDataType], classOf[valueDataType], conf)
```
