To run this program from the terminal, simply run the following command. The program will the then be compiled and executed.
`sbt "runMain training.rddToDs"`{{execute}}

The output is as shown in the screenshot below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 8/Selection_013.png)
 
The only difference between creating a DataFrame and a Dataset is the method which we call at the end. We use the toDF method to create a DataFrame and toDS method to create a dataset.

We can also use the programatical schema to create a dataset as we did with the DataFrame in Task 3 of previous exercise. Please try it out and create a dataset by programatically creating a schema.

Task is complete!


