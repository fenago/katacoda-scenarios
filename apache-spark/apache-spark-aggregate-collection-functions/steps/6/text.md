

**Step 5:** Let us call the show method and run the program.

```
aggAlias.show()
```

The following result should be shown.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 8/Selection_020.png)

As you can see from the screenshot above, the column names appear as we have specified.

**Step 6:** Let us now use the groupBy method and perform the aggregations.

```
val byUser = movies.groupBy("userId")
  .agg(countDistinct("rating").as("distinctCount")
    , sumDistinct("rating").as("distinctSum")
    , count("movieId").as("movieCount"))
```

In the code above, we have used the groupBy method and performed the aggregations over the group. We have used the countDistinct function to count the number of distinct ratings for userId. Similarly, the sumDistinct function to sum to only sum the distinct ratings. Finally, count function as you know, is used to count all the movie ids.

 

**Step 7:** Let us call the show method and run the program.

```
byUser.show()
```


#### Compile and Run
To run this program from the terminal, simply run the following command. The program will the then be compiled and executed.
`sbt "runMain training.builtInFunctions"`{{execute}} 

The following result should be shown.

 