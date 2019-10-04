
**Step 5:** Remember, we have also wrapped all the good records in the Right object. We can use it in our if condition with else object here as well.

```
else {
  val goodRecords = parsedRecords.right.map(x => (x.userId, x.movieId, x.rating, x.timeStamp))
  goodRecords.foreach(println)
}
```

We are declaring a new variable called goodRecords and simply extracting (map) the fields from the Right object using the right method. Finally, we can print them out to the console in the next line.

 
**Step 6:** Let us now run it and see the good records as shown in the screenshot below.
`sbt "runMain training.counters"`{{execute}} 

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 6/Selection_013.png)

We have successfully implemented Accumulators and also separated good records with bad records.

Task is complete!
