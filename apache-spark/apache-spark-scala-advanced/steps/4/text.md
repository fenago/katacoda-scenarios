Let us first create a function that does not have any parameters or a return type. Enter into the paste mode in Scala console and execute the following code.

`:paste`{{execute}}

**Note:** After pasting following code in the scala terminal, Press  `Ctrl` + `D` to run code.

```def hello = {
println("Hello there!")
}```{{execute}}

Now, simply call this function by its name.
`hello`{{execute}}

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 2/Selection_039.png) 

As you can see from the screenshot above, Scala has automatically inferred the return type as unit which means no return type. Unit is similar to that of Void in Java.
