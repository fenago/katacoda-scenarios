

**Step 4:** Let us now declare our Accumulator object. The Accumulator object in Spark 2.x is a bit different from what we have seen in Spark 1.x. There are two types of Accumulators we can use in 2.x. They are the longAccumulator and doubleAccumulator. As their names suggest a longAccumulator is used for Long data type and doubleAccumulator for Double data type. 

We shall be using longAccumulator in our code as we only need the count of type Long. 

```
val badRecords = sparkSession.sparkContext.longAccumulator("Bad Records")
```

The longAccumulator object is wrapped in the sparkContext object which in turn is wrapped with the sparkSession object. The initial value for longAccumulator is set to zero (0) by default. We need not initiate it as we did in Spark 1.x API for Accumulator. All we need to do is set a name for our Accumulator. We have named it Bad Records. You are free to use any name as you like.

 