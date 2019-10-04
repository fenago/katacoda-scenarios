Apache Spark is an open source, fast and unified parallel large-scale data processing engine. It provides a framework for programming with distributed processing of large datasets at high speed. Spark supports most popular programming languages such as Java, Python, Scala and R. 

Spark is scalable, meaning, it can run on a single desktop machine or a laptop to a cluster of thousands of machines. Spark provides a set of inbuilt libraries which can be accessed to perform data analysis over a large dataset. However, if your requirement doesn’t get satisfied with the inbuilt libraries, you can write one or explore countless external libraries from open source communities on the internet.


#### Why Spark?

Why use Spark when we have Hadoop? Well, Spark excels as a unified platform for processing huge data at very high speeds for various data processing requirements (will be discussed later in this chapter). Also, Spark is an in-memory processing framework. Spark is considered as a successor of Apache Hadoop. Let us briefly discuss the advantages of Spark over Hadoop.


#### Data Processing with Spark

In Spark, the data is read from the disk, processed in-memory but instead of spilling it back to disk, Spark can retain the data within the memory for further processing. So, if the processed data is again required for further processing, the data is already present in the memory and the Spark application processes the data eliminating the IO latency and therefore the overall time to process the job is significantly reduced. 

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/spark.JPG)
