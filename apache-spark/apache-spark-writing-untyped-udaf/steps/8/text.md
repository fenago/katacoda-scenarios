
**Step 7:** Now that we have set our input, buffer and output schema, we have to initialize our buffer (0, 0) using the initialize method.
 
```
def initialize(buffer: MutableAggregationBuffer): Unit = {
  buffer(0) = 0.00
  buffer(1) = 0L
```

The initialize method takes buffer of type MutableAggregationBuffer and returns nothing. The MutableAggregationBuffer as the name suggests is mutable and is used for aggregation purposes. The two columns in the buffer sum and count are initialized to 0. The first buffer is of type Double and second is of type Long.

**Step 8:** At this point of time, we have specified schema for input, buffer and output. We have also initialized the buffer with zero. We now have to write the logic so that tasks know how to update the buffer.

We do this using the update method as shown below.

```
def update(buffer: MutableAggregationBuffer, input: Row): Unit = {
  if (!input.isNullAt(0)) {
    buffer(0) = buffer.getDouble(0) + input.getDouble(0)
    buffer(1) = buffer.getLong(1) + 1
  }
}
```

The update method takes two parameters. One is the buffer which we have initialized and the actual input (which is ratings in our case). The first buffer simply adds the ratings and the second buffer increments the count by 1 until all the records are processed. This update method is applied to every task processing this job. After the update method completes processing , there will be a final output buffer for each task. All we have to do is to merge the output of each task, which is what we are going to do in the next step.

