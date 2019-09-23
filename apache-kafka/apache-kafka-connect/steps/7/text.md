Now, what we are going to do is to calculate the uptimes. As is to be expected, Spark does not have a built-in function to calculate the number of days between two dates, so we are going to create a user-defined function.

To achieve this, the first thing we do is build a function that receives as input a java.sql.Timestamp, as shown in the following code (this is how timestamps are represented in the Spark DataSets) and returns an integer with the number of days from that date:

```
private final int uptimeFunc(Timestamp date) {
    LocalDate localDate = date.toLocalDateTime().toLocalDate();
    return Period.between(localDate, LocalDate.now()).getDays();
}
```

The next step is to generate a Spark UDF as follows:

```
Dataset<Row> processedDs = healthCheckDs
    .withColumn( "lastStartedAt", new Column("uptime"));
```
And finally, apply that UDF to the lastStartedAt column to create a new column in the Dataset called uptime.