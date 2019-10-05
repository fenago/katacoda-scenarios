If you do not want the last iteration to be included, you can use the keyword until instead of to. For example,

`:paste`{{execute}}


**Note:** After pasting following code in the scala terminal, Press  `Ctrl` + `D` to run code.

```for ( i <- 1 until 5) {
	val sum = i + i
	println(sum)
}```{{execute}}


 
We can also use an if statement within the for loop as shown below.

`:paste`{{execute}}

**Note:** After pasting following code in the scala terminal, Press  `Ctrl` + `D` to run code.

```val friends = List("Chandler", "Monica", "Rachel", "Ross", "Joey", "Phoebe")
for(friend <- friends if friend == "Chandler"){
println(s"The king of sarcasm is $friend")
}```{{execute}}

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 2/Selection_035.png)

In the above example, we are looping through the list of collection called friends, with an if condition. We filter out all the items except for one element and substitute the variable in the print statement. Please see that we are using double equals operator to compare two strings.
