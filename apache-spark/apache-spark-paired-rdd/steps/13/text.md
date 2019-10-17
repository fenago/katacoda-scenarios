

**Step 4:** We can now use the collect function to collect the final result from the RDD and display it on the console using the following line of code. This action triggers DAG and the job is executed.

```
avgRatings.collect.foreach(println)
```
 
**Important:** You need to uncomment above line in `avgRatings.scala` using **vscode** editor before running program again.

**Step 5:** To run this program from the terminal, simply run the following command. The program will the then be compiled and executed.

`sbt "runMain training.avgRatings"`{{execute}} 

Once the job is finished, check the output in the console as shown in the screenshot below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 5/Selection_023.png)