
**Step 3:** Let us now implement the methods from the Aggregator abstract class. The first method is the zero method which initializes the buffer to zero. This is similar to initialize method which we have used in the previous task.

```
def zero: Average = Average(0, 0L)
```

**Step 4:** Next, we have to implement the reduce method which is similar to update method used in the previous task. The reduce method provides the logic to specify how the tasks should process the rows and columns of dataset.

```
def reduce(buffer: Average, rat: Ratings): Average = {
  buffer.sum += rat.rating
  buffer.count += 1
  buffer
}
```

The reduce method takes the buffer which is of type Average and the input ratings. The buffer is then updated for each row in the rating column along with the count. Once all the records are processed, the final value of the buffer for each task is returned.

At this point, we have buffer outputs of each task. We now have to merge them to get the final sum and count of all the records.
