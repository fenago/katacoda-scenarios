
 

**Step 4:** Let us now use some more math functions.

val mathFuncs2 = numbersDS.select(factorial($"numbers"), floor($"numbers"), hex($"numbers"), log($"numbers"))

●	The factorial functions returns the factorial of the number.

●	The floor function is opposite to the ceil function which returns the number of double type lesser than or equal to the nearest rounded integer.

●	The hex function returns a hex value.

●	The log function returns the natural logarithm (base e) of a double value as a parameter.

Let us check the result using the show method.

mathFuncs2.show()
 

The following result is shown.

 