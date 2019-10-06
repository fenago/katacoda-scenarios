

**Step 5:** Let us now use even more math functions.

`val mathFuncs3 = numbersDS.select(pow($"numbers", 2), round($"numbers"), sin($"numbers"), tan($"numbers"))`{{execute}} 

- The pow function returns the number raised to the power of some other number. It takes two arguments. The first argument is the column with numbers and the second argument is number which the power has to be calculated.

- The round function returns the rounded value to its nearest decimal.

- The sin and tan functions return the sine and tangent trignometric angle respectively.

Let us check the result using the show method.
`mathFuncs3.show()`{{execute}} 

The following result is shown.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 8/Selection_043.png)


**Step 6:** Let us finally conclude math functions with a couple more of them.

`val mathFuncs4 = numbersDS.select(sqrt($"numbers"), log10($"numbers"), $"numbers" + Math.PI)`{{execute}} 

- The sqrt function returns the square root of the given numbers in the column.

- The log10 function returns the base 10 logarithm of a double value.

- In the third column, we have simply added the value of PI by using the Math.PI expression.

Let us check the result using the show method.
`mathFuncs4.show()`{{execute}} 


The following result is shown.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 8/Selection_044.png)

 

