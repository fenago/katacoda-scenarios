Why use Spark when we have Hadoop? Well, Spark excels as a unified platform for processing huge data at very high speeds for various data processing requirements (will be discussed later in this chapter). Also, Spark is an in-memory processing framework. Spark is considered as a successor of Apache Hadoop. Let us briefly discuss the advantages of Spark over Hadoop.


#### Data Processing with Spark

In Spark, the data is read from the disk, processed in-memory but instead of spilling it back to disk, Spark can retain the data within the memory for further processing. So, if the processed data is again required for further processing, the data is already present in the memory and the Spark application processes the data eliminating the IO latency and therefore the overall time to process the job is significantly reduced. 

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/spark.JPG)
