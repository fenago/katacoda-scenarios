**Step 6:** We can also extract the keys and values to separate RDDs as shown below.

```
val RDDKeys = flattened.keys

RDDKeys.collect.foreach(println)
```

Similarly, we can extract the values using the code below.

```
val RDDValues = flattened.values

RDDValues.collect.foreach(println)
```
 
**Important:** You need to uncomment above line in `tags.scala` using **vscode** editor before running program again.

`sbt "runMain training.tags"`{{execute}} 

Task is complete!

