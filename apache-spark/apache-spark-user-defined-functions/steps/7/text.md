

**Step 4:** Let us call the UDF decrUDF using the DataFrame API using the select method, as shown below.

```
val ratingDecDf = ratings.select($"*", decrUDF($"rating").as("ratingDec"))
```

Here, we are selecting all the columns from our dataset and then adding one more column called ratingDec, which is obtained by applying our UDF on rating column.

Let us finally call the show method to check the output.

```
ratingDecDf.show()
```

 
#### Compile and Run
To run this program from the terminal, simply run the following command. The program will the then be compiled and executed.
`sbt "runMain training.decrRatingUDF"`{{execute}} 

The output should be displayed as shown in the screenshot below, when you run the program.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 9/Selection_015.png)


Please see that we need not register the UDF using the `udf.register` method when we have declared a function literal within the udf function. However, we must register our UDF when he have not used the function literal and defined the UDF using the def keyword. We shall look at this in the next few steps.
