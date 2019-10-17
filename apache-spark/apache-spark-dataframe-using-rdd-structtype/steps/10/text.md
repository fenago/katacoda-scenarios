
**Step 6:** Finally, we can use our RDD which is structRecords and schema as parameters for createDataFrame method to create a dataFrame.

```
val recordsDf = ss.sqlContext.createDataFrame(structRecords, schema)
```

Since `createDataFrame` is a method of sqlContext object we call sqlContect on our SparkSession object and then call createDataFrame method.

Let us use the show method to check the created dataFrame using createDataFrame method.

```
recordsDf.show()

  }

}
```
