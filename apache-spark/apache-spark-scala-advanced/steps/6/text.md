**Step 3:** Let us now look at Higher Order Functions. Higher Order functions are the functions which take other functions as parameters. Let us understand this with an example.

In the scala console, enter the following code.

```def squared (num: Int) : Int = {
num * num
}```{{execute}} 

You can call the function square to see if it works. For example,
`squared(5)`{{execute}} 
 
 

Now, let us pass this function as a parameter to another function.

```def highSquared(num: Int, func: Int => Int): Int = {
	func(num)
	}```{{execute}} 

Here, we are defining a function named highSquared which takes two parameters and returns an Int. One of them is an integer named num and the another one is function named func which takes a parameter of type Int and returns an Int. In the function body, The function func takes the value of num and returns its value. Let us call this function.

`val result = highSquared(4, squared)`{{execute}} 

`println(result)`{{execute}} 

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 2/Selection_043.png) 

