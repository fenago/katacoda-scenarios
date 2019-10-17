**Step 1:** Navigate back to the counters object in IDE and continue from where we left in Task 1.

**Step 2:** Let us now write a foreach action which parses each row through our recordParser object, which we have implemented in the previous task.

```
data.foreach(row => {
  val parsedRecords = recordParser.parse(row)
  if(parsedRecords.isLeft){
    badRecords += 1
  }
})
```

We then write a if condition to check if the record is a left object i.e., a bad record. If it is, we simply increment the value of badRecords variable which we declared in task 1 by 1.

We can use the isLeft method to check if it is a Left object and isRight method for Right object.


Please see that we are using foreach function, which is a action and not a transformation. As learned in the theory section, Accumulators should always be specified in the action part and not in the transformations. This way we can be sure that our accumulator is only processed once and the value is accurate.

At this point, we have successfully implemented counters based on our requirement. All we need to do now is to simply get the final accumulated value.
