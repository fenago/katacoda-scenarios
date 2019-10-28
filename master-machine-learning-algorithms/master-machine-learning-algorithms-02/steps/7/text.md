
We now have the parts for calculating the numerator. All we need to do is multiple the error
for each x with the error for each y and calculate the sum of these multiplications.

x - mean(x) | y - mean(y) |  Multiplication
--- | --- | ---
-2 |  -1.8  | 3.6
-1  | 0.2  | -0.2
1  | 0.2  | 0.2
0  | -0.8  | 0
2  | 2.2  | 4.4

Multiplication of the x and y residuals from their means.

Summing the final column we have calculated our numerator as 8. Now we need to calculate
the bottom part of the equation for calculating B1, or the denominator. This is calculated as
the sum of the squared differences of each x value from the mean. We have already calculated
the difference of each x value from the mean, all we need to do is square each value and calculate
the sum.

x - mean(x) | squared
--- | ---
-2  | 4
-1  | 1
1   | 1
0   | 0
2   | 4

Squared residual of each x value from the mean.

Calculating the sum of these squared values gives us a denominator of 10. Now we can
calculate the value of our slope.

```
B1 = 8/10

B1 = 0.8
```
