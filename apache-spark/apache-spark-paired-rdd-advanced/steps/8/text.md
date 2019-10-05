**Step 6:** We can also extract the keys and values to separate RDDs as shown below.

```
val RDDKeys = flattened.keys

RDDKeys.collect.foreach(println)
```

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 5/Selection_033.png)

Similarly, we can extract the values using the code below.

```
val RDDValues = flattened.values

RDDValues.collect.foreach(println)
```

**Important:** You need to uncomment above line in `tags.scala` using **vscode** editor before running program again.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 5/Selection_034.png)


`sbt "runMain training.tags"`{{execute}} 

Task is complete!

