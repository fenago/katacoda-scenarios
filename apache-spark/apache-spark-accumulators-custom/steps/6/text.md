

**Step 6:** The next step is to implement the merge method which actually aggregates all the values from executors and provides with the final count.

```
def merge(tuples: AccumulatorV2[(Int, Int), HashMap[Int, Int]]): Unit = {

  tuples.value.foreach(add)

}

def value() =  movieCount
```

When all the tasks complete executing, the final results from all the executors is then sent to the driver where the merging happens. The merge method takes an AccumulatorV2 as an argument which takes a tuple and returns a HashMap as output. The merge method is called on all the local accumulators from the tasks processed in the exectors. Therefore, we use the  add method inside the foreach function.
Since we declared the HashMap as private, we can only access it through the value method. The value method is used to simply get the current value in our accumulator.

To summarize, the merge method takes an accumulator as an argument and merges all the local accumulators, which were processed in the executors by tasks, based on the logic in add method, into the global accumulator. The value method is used to get the current value of the HashMap variable movieCount.



 