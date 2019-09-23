As we already processed the data and calculated the uptime, now all we need to do is to write these values in the Kafka topic called uptimes.

Kafka's connector allows us to write values to Kafka. The requirement is that the Dataset to write must have a column called key and another column called value; each one can be of the type String or binary.

Since we want the machine serial number to be the key, there is no problem if it is already of String type. Now, we just have to convert the uptime column from binary into String.

We use the select() method of the Dataset class to calculate these two columns and assign them new names using the as() method, shown as follows (to do this, we could also use the alias() method of that class):

```
Dataset<Row> resDf = processedDs.select(
    (new Column("serialNumber")).as("key"),
    processedDs.col("uptime").cast(DataTypes.StringType).as("value"));
```

Our Dataset is ready and it has the format expected by the Kafka connector. The following code is to tell Spark to write these values to Kafka:

```
//StreamingQuery kafkaOutput =
resDf.writeStream()
   .format("kafka")
   .option("kafka.bootstrap.servers", brokers)
   .option("topic", "uptimes")
   .option("checkpointLocation", "/temp")
   .start();
```

Note that we added the checkpoint location in the options. This is to ensure the high availability of Kafka. However, this does not guarantee that messages are delivered in exactly once mode. Nowadays, Kafka can guarantee exactly once delivery; Spark for the moment, can only guarantee the at least once delivery mode.

Finally, we call the awaitAnyTermination() method, shown as follows:

```
try {
  spark.streams().awaitAnyTermination();
} catch (StreamingQueryException e) {
  // deal with the Exception
} 
```

An important note is to mention that if Spark leaves a console output inside the code, it implies that all queries must call its start() method before calling any awaitTermination() method, shown as follows:

```
firstOutput = someDataSet.writeStream
...
    .start()
...
 secondOutput = anotherDataSet.writeStream
...
    .start()
firstOutput.awaitTermination()
anotherOutput.awaitTermination()
```

Also note that we can replace all the `awaitTermination()` calls at the end with a single call to `awaitAnyTermination()`, as we did in the original code.