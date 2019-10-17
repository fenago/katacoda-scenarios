**Step 3:** Let us now look at while and do while loops. The while construct is similar to that of other programming languages. However, in functional programming, the use of while loops is discouraged. 

Enter into the paste mode and execute the following code.

`:paste`{{execute}}

**Note:** After pasting following code in the scala terminal, Press  `Ctrl` + `D` to run code.

```
var friends = 0

val names = List("Chandler", "Monica", "Rachel", "Phoebe", "Ross", "Joey")

println("The names of friends are:")

while (friends < 6){

println(s"${names(friends)}")

friends += 1

}```{{execute}}

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 2/Selection_036.png)

In the code above, we have first declared an Integer variable with a value of 6 and then a list of names of type String. Next, we print out a header so that the output makes sense and then write the While loop. The loop starts with a keyword while and then the condition inside the parentheses. The condition we set here is to continue the loop until value of friends is less than 6. Next, we use String interpolation to substitute the variables within the print statement. Please see that we have used curly braces, as we have substituted a variable named friends as a value to the variable  names. So that every time the loop runs, we are accessing each element of the list by its index starting from 0. Finally we increment the variable friends with 1.

The while loop runs every time the condition is satisfied and only comes out of the loop when the condition is false.