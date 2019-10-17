
**Step 3:** Let us use the println function to print the number of bad records in our input dataset.

```
println("The number of bad records in the input are  " + badRecords.value)
  }

}
```

To retrieve the value from our accumulator which is badRecords, we use the value  method. You cannot directly retrieve the value just by using the badRecords variable when it comes to Accumulators.

 

**Step 4:** Finally, let us run our code and check the output. You should see the number of bad records as shown in the screenshot below.

To run this program from the terminal, simply run the following command. The program will the then be compiled and executed.
`sbt "runMain training.counters"`{{execute}} 

 
With this we have successfully impemented Accumulators using Spark 1.x API.


