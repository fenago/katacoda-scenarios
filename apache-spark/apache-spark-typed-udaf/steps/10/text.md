
**Step 9:** Let us now use of UDAF we wrote in this task. We have to call the toColumn method on our UDAF and give it a name using the name method as shown below.

```
val averageRating = averageTypedUDAF.toColumn.name("averageRating")
```

Let us now use the select method for the UDAF as shown below.

```
val avg = ds.select(averageRating)
```

Finally, let us call the show method and run the program.

```
avg.show()
```

#### Compile and Run
To run this program from the terminal, simply run the following command. The program will the then be compiled and executed.
`sbt "runMain training.avgTypedUADF"`{{execute}} 

The output which calculates average of all the ratings is as shown in the screenshot below.
 
![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 9/Selection_034.png) 
 

This completes the Typed UADF task.

Task is complete!
