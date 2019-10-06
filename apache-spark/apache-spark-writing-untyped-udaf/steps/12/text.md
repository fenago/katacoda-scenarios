**Step 4:** Let us finally use the UDAF in our SQL query as shown below.

```
val average = sparkSession.sql("SELECT userId,  averageUDAF(rating) AS avgRating FROM ratings GROUP BY userId")
```

Let us check the result using the show method as shown below

```
average.show()
```


#### Compile and Run
To run this program from the terminal, simply run the following command. The program will the then be compiled and executed.
`sbt "runMain training.avgRatingUDAF"`{{execute}} 

The following output is shown.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 9/Selection_029.png)
 
We have successfully written a UDAF, registered and used it in the Spark application.

Task is complete!
