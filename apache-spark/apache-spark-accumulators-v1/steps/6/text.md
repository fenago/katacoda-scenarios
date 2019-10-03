**Step 5:** The next step is to use the accumulator method in the SparkContext object and pass its arguments. The arguments are the initial value of zero (0) and the name of our accumulator as bad records.

```
val badRecords = sc.accumulator(0, "bad records")
```

You will see a warning "Symbol Accumulator is deprecated". You may ignore this warning as this is older Accumulator API for Spark 1.x.
