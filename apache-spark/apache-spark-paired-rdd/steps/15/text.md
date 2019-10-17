You can also sort the result by the key by referring the first element in the sortBy function or simply using the sortByKey function key as shown below.

```
val sorted = avgRatings.sortByKey()
```

Finally, you can sort the results in descending order when sortByKey is used by passing argument as false for the function.

```
val sorted = avgRatings.sortByKey(false)
```

Task is complete!


**Important:** You can run all of above one by one be editing `avgRatings.scala` using **vscode** editor before running program.

To run the program from the terminal, simply run the following command. The program will the then be compiled and executed.

`sbt "runMain training.avgRatings"`{{execute}} 
