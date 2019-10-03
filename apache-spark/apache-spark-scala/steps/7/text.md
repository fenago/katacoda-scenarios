
You can check if the declared variable is immutable by trying to append a new String to the name variable which we created previously as shown below.
 

`name = name + " Inc"`{{execute}} 

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 2/Selection_018.png)

As you can see from the screenshot above, it throws an error saying reassignment to val, which means you cannot reassign or modify an immutable variable.

