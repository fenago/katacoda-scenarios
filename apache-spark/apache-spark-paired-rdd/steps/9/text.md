**Step 3:** Finally let us create our pairedRDD. To do this, we have to pass the parseRecords function as an argument to the map higher order function so that all the records in the data RDD are parsed as per the logic in our parseRecords function. The following line of code does that work.

```
val RDDPair = data.map(parseRecords)
```

That's it. We now have our paired RDD. You can optionally take a look at the RDDPair by simply printing it out to the console using the code below.

```
 RDDPair.collect.foreach(println)
```

PS: Using collect is not recommended if your data is very big. When collect is used, all the data is shuffled to the driver node and if there is not enough memory available in the driver node, the job will throw an memory exception error.

#### Compile and Run
To run this program from the terminal, simply run the following command. The program will the then be compiled and executed.

`sbt "runMain training.avgRatings"`{{execute}} 

You should have the output in the console with the key-value pairs as shown in the screenshot below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 5/Selection_016.png)

The first element in the tuple is the key (userId) and the second element in the tuple is a value (ratings).

Task is complete!

