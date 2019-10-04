Parquet is a widely used file format in Spark because of the optimizations it provides for analytical processing and is considered as one of the most efficient file formats for Spark. Parquet is column-oriented data structure and is the default file format in Spark. When no format is specified, Spark automatically process them as Parquet. Parquet is compressable, splittable but is not human readable. Parquet supports complex data structures. It can be easily processed when columns are of struct, map or array type. This is not possible with JSON and CSV files.


Parquet has only a couple of options while reading and writing the data. The following is an example to read a Parquet file.

```
spark.read
.format("parquet")
.load("/usr/local/files/sample.parquet")
```

We can also read without specifying the schema as shown below.

```
spark.read
.load("/usr/local/files/sample.parquet")
```
