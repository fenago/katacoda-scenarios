There are several connectors for Apache Spark. In this case, we are using the Databricks Inc. (the company responsible for Apache Spark) connector for Kafka.

Using this Spark Kafka connector, we can read data with Spark Structured Streaming from a Kafka topic:

```
 Dataset<Row> inputDataset = spark
    .readStream()
    .format("kafka")
    .option("kafka.bootstrap.servers", brokers)
    .option("subscribe", Constants.getHealthChecksTopic())
    .load();
````

Simply by saying Kafka format, we can read a stream from the topic specified in the subscribe option, running on the brokers specified.


As with Kafka Streams, with Spark Streaming, in each step we have to generate a new data stream in order to apply transformations and get new ones.

In each step, if we need to print our data stream (to debug the application), we can use the following code:

```
StreamingQuery consoleOutput =
    streamToPrint.writeStream()
    .outputMode("append")
    .format("console")
    .start();
```

The first line is optional, because we really don't need to assign the result to an object, just the code execution.