
**Step 4:** Now that we have our dataFrames, let us create a temp view so that we can run our join query against them.

```
movies.createOrReplaceTempView("movies")
ratings.createOrReplaceTempView("ratings")
```

**Step 5:** We now have our views. All we need to do now is to perform the join. We can join this using the SQL query as shown below.

```
val joinedDf = spark.sql("SELECT * FROM movies JOIN ratings ON movies.movieId = ratings.movieId"
```

Finally, let us call the show method on our joinedDf dataFrame and run the program.

```
joinedDf.show()
```


To run this program from the terminal, simply run the following command. The program will the then be compiled and executed.
`sbt "runMain training.sqlJoins"`{{execute}} 

You should see the joined table as shown in the screenshot below.

Task is complete!

 
