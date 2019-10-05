Dataset is the most advanced API in Spark. Datasets are an extension of DataFrames, which overcome all the disadvantages of both RDDs and DataFrames. The Dataset API provides developers with type safe mechanism and functional style programming, while retaining the relational type of programming in DataFrames and performance optimizations. Hence it is called as an extension of DataFrames. Datasets were introduced in Spark from the 1.6 version.

Datasets use Encoders to serialize and deserialize the Spark SQL representation to JVM objects. The serialization and deserialization with encoders is significantly fast when compared to Java serialization. In simple words, datasets use encoders to convert the data between JVM objects and Spark SQL representation of tabular objects.


#### Why Datasets?

The following are the advantages of using datasets.

- Datasets are a combination of RDDs and DataFrames. Datasets help you code like you would with RDDs and process them through performance optimization engines.

-  Datasets have all the other features as RDD and DataFrames. They are lazy, immutable, distributed and can be cached.

- Datasets assures type safety similar to that of RDD. Any type errors are flagged at compile time rather than being notified at runtime.

- Data processing with datasets is optimized using the Catalyst optimizer and Tungsten similar to that of DataFrames. This ensures very fast and efficient processing of data.

- Dataset API provides the developers with a functionaly style of programming as well as relational style of programming.

- Datasets can process structured as well as unstructured data. Datasets can also automatically infer schema.

- Datasets can be converted from RDD and DataFrames. 
