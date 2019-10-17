Spark SQL is a library or module of Spark, which provides SQL style programming to process structured data. Spark SQL runs on top of Spark by wrapping all the Spark core APIs into a high level abstraction. Spark SQL also provides optimizations to run the jobs faster which lacks in Spark core making Spark even more efficient. Since Spark SQL is syntactically similar to SQL, it is easier for developers, who already work on SQL to become productive faster with less efforts. Spark SQL was implemented to overcome the disadvantages of running Apache Hive on top of Spark.


##### Why Spark SQL?

The following are the advantages of using Spark SQL.

- Spark SQL is popular because, it provides developers with an easy to use APIs with support to various data sources. Spark SQL provides interfaces for programming languages and query languages which include SQL and HiveQL, helping developers to get productive in no time.

- A wide variety of file formats such as csv, Avro, Json, Parquet, ORC etc are supported by Spark SQL. It also supports almost all the relational databases with JDBC connectivity, which include MySQL, Postgress, Oracle to name a few. NoSQL datastores such as Hbase, Cassandra, EasticSearch are also supported with Spark SQL.

- Spark SQL can also be easily integrated to other Spark libraries, which include Spark ML, graphX and Spark Streaming.

- Spark SQL efficiently processes structured data by advanced optimization techniques such as cost based optimizer, in-memory columnar caching, code generation and reduced disk IO. 
In view of all these features, it is recommended to use Spark SQL (Data Frames) over RDDs whenever possible.
