
**Step 3:** Let us now perform various math functions on the dataset. All these functions are self explanatory.

`val mathFuncs1 = numbersDS.select(abs($"numbers"), ceil($"numbers"), exp($"numbers"), cos($"numbers"))`{{execute}} 

- The abs function returns the absolute value of the number.

- The ceil function returns the number of double type greater than or equal to the nearest rounded integer. 

- The exp function returns Eulers E raised to power of double value.

- The cos function returns the trigonometric cosine of an angle.

Let us check the result using the show method.

`mathFuncs1.show()`{{execute}} 

The following result is shown.

![](https://github.com/athertahir/apache-spark/raw/master/Screenshots/Chapter 8/Selection_040.png)

 

