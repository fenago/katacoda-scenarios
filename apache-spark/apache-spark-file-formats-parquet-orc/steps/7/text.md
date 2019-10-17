ORC is yet another columnar file format which stands for Optiimized Row columnar. There are no options for ORC files because Spark processes ORC file format very efficiently. Both ORC and Parquet are similar but Parquet is very much optimized for Spark and ORC is optimized for Hive. 

ORC supports complex data structures, is splittable and can be compressed. ORC is not human readable. The following shows an example of reading an ORC file.

```
spark.read
.format("orc")
.load("/usr/local/files/sample.orc")
```

