Sequence file is the popular Hadoop file format which contains keys and values in binary form. We can read Sequence files using the sequenceFile method on the SparkContext object and, write them using the saveAsSequenceFile method on the RDD.

The syntax to read the file is

```
sparkContext.sequenceFile("/path/to/seq/file", classOf[keyDataType], classOf[valueDataType])
```

As you can see in the syntax above, we also have to specify the data types of keys and values of the Sequence file using classOf[] object.

The syntax to write the file is

```
rdd.saveAsSequenceFile("/path/to/seq/output")
```

Please note that we cannot directly read or save a Sequence file using the DataSource API. We can however, convert the RDD loaded from Sequence file to a DataFrame using the toDF method. To save a DataFrame to Sequence File, we must create a paired RDD from a DataFrame and then use the saveAsSequenceFile method.
