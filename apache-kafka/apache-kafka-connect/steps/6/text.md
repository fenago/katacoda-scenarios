We know that when we produced the data, it was in JSON format, although Spark reads it in binary format. To convert the binary message to string, we use the following code:

```
Dataset<Row> healthCheckJsonDf =
    inputDataset.selectExpr("CAST(value AS STRING)");
```


The Dataset console output is now human-readable, and is shown as follows:

```
+--------------------------+
|                     value|
+--------------------------+
| {"event":"HEALTH_CHECK...|
+--------------------------+
 ```

The next step is to provide the fields list to specify the data structure of the JSON message, as follows:

```
StructType struct = new StructType()
    .add("event", DataTypes.StringType)
    .add("factory", DataTypes.StringType)
    .add("serialNumber", DataTypes.StringType)
    .add("type", DataTypes.StringType)
    .add("status", DataTypes.StringType)
    .add("lastStartedAt", DataTypes.StringType)
    .add("temperature", DataTypes.FloatType)
    .add("ipAddress", DataTypes.StringType);
```

Next, we deserialize the String in JSON format. The simplest way is to use the prebuilt from_json()function in the org.apache.spark.sql.functions package, which is demonstrated in the following block:

```
Dataset<Row> healthCheckNestedDs =
    healthCheckJsonDf.select(
        functions.from_json(
            new Column("value"), struct).as("healthCheck"));
```

If we print the Dataset at this point, we can see the columns nested as we indicated in the schema:

```
root
 |-- healthcheck: struct (nullable = true)
 |    |-- event: string (nullable = true)
 |    |-- factory: string (nullable = true)
 |    |-- serialNumber: string (nullable = true)
 |    |-- type: string (nullable = true)
 |    |-- status: string (nullable = true)
 |    |-- lastStartedAt: string (nullable = true)
 |    |-- temperature: float (nullable = true)
 |    |-- ipAddress: string (nullable = true)
```

The next step is to flatten this Dataset, as follows:

```
Dataset<Row> healthCheckFlattenedDs = healthCheckNestedDs
   .selectExpr("healthCheck.serialNumber", "healthCheck.lastStartedAt");
```

To visualize the flattening, if we print the Dataset, we get the following:

```
root
 |-- serialNumber: string (nullable = true)
 |-- lastStartedAt: string (nullable = true)
```

Note that we read the startup time as a string. This is because internally the from_json() function uses the Jackson library. Unfortunately, there is no way to specify the format of the date to be read.

For these purposes, fortunately there is the to_timestamp() function in the same functions package. There is also the to_date() function if it is necessary to read only a date, ignoring the time specification. Here, we are rewriting the lastStartedAt column, similar to this:

```
Dataset<Row> healthCheckDs = healthCheckFlattenedDs
    .withColumn("lastStartedAt", functions.to_timestamp(
        new Column ("lastStartedAt"), "yyyy-MM-dd'T'HH:mm:ss.SSSZ"));
```
