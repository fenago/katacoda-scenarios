**Step 4:** With the previous step all the transformations have been completed. Let us now perform an action to print out the result to console.

```
count.collect.foreach(println)
```

We can now simply use collect to collect the final RDD which is count and use foreach with println to print out each record in the RDD to the console. This will actually trigger the program to evaluate. All the trasnformations before this action are only logged in the Lineage graph to achieve lazy evaluation.

 

This completes our first ever Spark program. All we need to do now is to run it.
