
**Step 7:** Let us now register this new UDF by using the partially applied function as shown below. We have used the underscore placeholder to specify that this is a partially applied function for which the parameter will be passed later in the program.


```
spark.udf.register("decrUDF2", decrUDF2 _)

Let us also create a temporary table using createOrReplaceTempView function as shown below. We can then run our SQL queries over this table.

ratings.createOrReplaceTempView("ratings")

val ratingDecDf = spark.sql("select *, decrUDF2(rating) as ratingDec from ratings")
```

The program should look something like the screenshot shown below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 9/Selection_018.png)
 

**Step 8:** Let us finally call the show method and check the output.

```
ratingDecDf.show()
```

**Important:** You need to uncomment above line in `decrRatingUDF.scala` using **vscode** editor before running program again.

#### Compile and Run
To run this program from the terminal, simply run the following command. The program will the then be compiled and executed.
`sbt "runMain training.decrRatingUDF"`{{execute}} 


The following output is shown.
![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 9/Selection_019.png)


 
With this we have written, registered and use a UDF.

Task is complete!




