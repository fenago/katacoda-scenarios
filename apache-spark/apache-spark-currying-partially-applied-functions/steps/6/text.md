
**Step 3:** We can also define currying functions with multiple parameters inside each parameter group as shown below.

```def sumProd(a: Int, x: Int) (b: Int, y: Int): Int = {
	| a * b + x * y
	| }```{{execute}}
 

**Step 4:** We can also define a currying function in such a way that we can tranform a function which takes two or more parameters into a function that takes only one parameter.

`def prod(a: Int) = (b: Int) => a * b`{{execute}}

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 9/Selection_004.png) 

As you can see from the screenshot above, we have declared a prod function which only takes one parameter a and returns another function which in turn takes another parameter b and returns the result.
