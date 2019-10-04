**Step 2:** Let us now look at for loops. Enter in to the paste mode and execute the following code.

`:paste`{{execute}}

**Note:** After pasting following code in the scala terminal, Press  `Ctrl` + `D` to run code.

```for (i <- 1 to 5) {
	val sum = i + i
	println(sum)
}```{{execute}}

The syntax for the for loop is a bit unusual. We start the for loop with the for keyword and assign a range of 1 to 5 both inclusive to the variable i. The <- symbol is the range operator in Scala. Basically, it means that range of values between `1` and `5` are being assigned to the variable `i`  as a list of `1, 2, 3, 4, 5` and the loop is iterated through those values. Next we declare a variable called sum and add each value 1 through 5 with itself . Finally, we print the sum of values using the print line statement. The result is displayed with each value in a new line as shown in the screenshot below.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 2/Selection_033.png)