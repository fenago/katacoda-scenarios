
**Step 9:** To merge the output of all the tasks, we use the merge method as shown below.

```
def merge(buffer1: MutableAggregationBuffer, buffer2: Row): Unit = {
  buffer1(0) = buffer1.getDouble(0) + buffer2.getDouble(0)

  buffer1(1) = buffer1.getLong(1) + buffer2.getLong(1)
}
```

The merge method takes two buffers i.e., two outputs from each task. It simply adds two outputs and stores it back in buffer1. This is performed for all the buffers.

**Step 10:** At this point of time, we have one single output from merge method. It contains the sum of all records and their count. All we have to do is write a logic to find out the average. The average is nothing but the sum divided by total count. This is implemented using the evaluate method.

```
def evaluate(buffer: Row): Double = buffer.getDouble(0) / buffer.getLong(1)
```

With this we have completed writing our UDAF. The error below the object name should be gone by now.  It should look like the screenshot below.



Task is complete!





