**Step 6:** Let us run this program and check the output. You should see the schema as shown below.

To run this program from the terminal, simply run the following command. The program will the then be compiled and executed.
`sbt "runMain training.users"`{{execute}} 
 
As you can see, the schema been correctly discovered by Spark for each and every column in the dataFrame. Please note that if a column has values of more than one data type, Spark will infer it as String.
The output of dataFrame users is as shown below.

 
As you can see from the screenshot above, the header is displayed correctly along with the records.

**Step 7:** We can also select only one column or more than one column from the dataFrame and have it shown using the code below.

```
users.select("last_name").show()
```

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 7/Selection_008.png)

**Important:** You need to uncomment above line in `users.scala` using **vscode** editor before running program again.

`sbt "runMain training.users"`{{execute}} 

The output is as shown in the screenshot below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 7/Selection_009.png)


